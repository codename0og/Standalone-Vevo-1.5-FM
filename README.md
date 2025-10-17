# <p align=center> Standalone-Vevo-1.5-FM </p>
## <p align=center> Isolated from Amphion. Make sure to check them out: <br/> https://github.com/open-mmlab/Amphion ~ </p>

## Usage:
### 1. Install with: `install-vevo.bat`
> Note: Installs by default: `torch==2.0.1`, `torchvision==0.15.2` and `torchaudio==2.0.2` | `cu118` <br/> So if you encounter any issues ( idk, rtx 50xx series? ) you gotta adjust torch / cuda for your specific case.
<br/>Refer to this:
[Pytorch website](https://pytorch.org/get-started/previous-versions)

### 2. Run with: `run-vevo.bat`
( It'll download all necessary assets and models upon the first launch so don't freak out if it " freezes " ) 
<br/><br/>You'll be asked for Reference voice path ( Path to your voice input / input speaker | .wav or .flac )
> Or you can skip it by pressing enter to use default path ( input_reference_voice folder, put your .wav or .flac file there. )

<br/>Next, you'll be asked for Content voice path ( Path to whatever you want your voice to sing / speak | .wav or .flac )
> Or you can skip it by pressing enter to use default path ( input_content folder, put your .wav or .flac file there. )

<br/>***And that's it. The output will land in: `output_conversion`***
<br/>
### Notes:
### 1. Total size after installation of env and downloading models is around 11-12 gig
### 2. Can't seem to figure out the AR mode, ( there seems to be some config issues ) <br/>hence it's marked by me as non-functional. <br/> If you come up with a solution, feel free to pr.
### 3. I most likely won't be improving or upgrading it. Isolated vevo for my own convenience ~
