# Copyright (c) 2023 Amphion.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import os
import glob
from huggingface_hub import snapshot_download

from models.svc.vevosing.vevosing_utils import *


def vevosing_fm(content_wav_path, reference_wav_path, output_path, shifted_src=True):
    gen_audio = inference_pipeline.inference_fm(
        src_wav_path=content_wav_path,
        timbre_ref_wav_path=reference_wav_path,
        use_shifted_src_to_extract_prosody=shifted_src,
        flow_matching_steps=32,
    )
    save_audio(gen_audio, output_path=output_path)


def find_first_audio_file(path, extensions=['.wav', '.flac']):
    if os.path.isdir(path):
        for ext in extensions:
            files = glob.glob(os.path.join(path, f"*{ext}"))
            if files:
                return files[0]

        print(f"Warning: Directory '{path}' was provided but no supported audio files ({', '.join(extensions)}) were found. Proceeding with directory path...")
        return path
    return path

def load_inference_pipeline():
    # ===== Device =====
    device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")

    # ===== Content-Style Tokenizer =====
    local_dir = snapshot_download(
        repo_id="amphion/Vevo1.5",
        repo_type="model",
        cache_dir="./ckpts/Vevo1.5",
        allow_patterns=["tokenizer/contentstyle_fvq16384_12.5hz/*"],
    )
    contentstyle_tokenizer_ckpt_path = os.path.join(
        local_dir, "tokenizer/contentstyle_fvq16384_12.5hz"
    )

    # ===== Flow Matching Transformer =====
    model_name = "fm_emilia101k_singnet7k"

    local_dir = snapshot_download(
        repo_id="amphion/Vevo1.5",
        repo_type="model",
        cache_dir="./ckpts/Vevo1.5",
        allow_patterns=[f"acoustic_modeling/{model_name}/*"],
    )

    fmt_cfg_path = f"./models/svc/vevosing/config/{model_name}.json"
    fmt_ckpt_path = os.path.join(local_dir, f"acoustic_modeling/{model_name}")

    # ===== Vocoder =====
    local_dir = snapshot_download(
        repo_id="amphion/Vevo1.5",
        repo_type="model",
        cache_dir="./ckpts/Vevo1.5",
        allow_patterns=["acoustic_modeling/Vocoder/*"],
    )

    vocoder_cfg_path = "./models/svc/vevosing/config/vocoder.json"
    vocoder_ckpt_path = os.path.join(local_dir, "acoustic_modeling/Vocoder")

    # ===== Inference =====
    inference_pipeline = VevosingInferencePipeline(
        content_style_tokenizer_ckpt_path=contentstyle_tokenizer_ckpt_path,
        fmt_cfg_path=fmt_cfg_path,
        fmt_ckpt_path=fmt_ckpt_path,
        vocoder_cfg_path=vocoder_cfg_path,
        vocoder_ckpt_path=vocoder_ckpt_path,
        device=device,
    )
    return inference_pipeline


if __name__ == "__main__":
    DEFAULT_REFERENCE_DIR = "./input_reference_voice"
    DEFAULT_CONTENT_DIR = "./input_content"
    DEFAULT_OUTPUT_FILENAME = "vevo_conversion_output.wav"

    inference_pipeline = load_inference_pipeline()

    ref_input = input(
        f"Enter path for the REFERENCE voice (Timbre/Style) [Default folder: {DEFAULT_REFERENCE_DIR}]: "
    )
    raw_reference_path = ref_input if ref_input else DEFAULT_REFERENCE_DIR

    content_input = input(
        f"Enter path for the CONTENT voice (Source Audio) [Default folder: {DEFAULT_CONTENT_DIR}]: "
    )
    raw_content_path = content_input if content_input else DEFAULT_CONTENT_DIR


    reference_wav_path = find_first_audio_file(raw_reference_path)
    content_wav_path = find_first_audio_file(raw_content_path)


    output_dir = "./output_conversion"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, DEFAULT_OUTPUT_FILENAME)

    print(f"\nRunning conversion...")
    print(f"Reference File: {reference_wav_path}")
    print(f"Content File: {content_wav_path}")
    print(f"Output Path: {output_path}")

    vevosing_fm(
        content_wav_path=content_wav_path,
        reference_wav_path=reference_wav_path,
        output_path=output_path,
        shifted_src=True,
    )

    print("\nConversion finished successfully!")