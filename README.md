# sue_checksum

Generates corresponding .sue checksums from .img image for BlackVue DR590W firmware.

```
$ sha256sum original_kernel_DR590W.img.sue generated_kernel_DR590W.img.sue
35ce0f42e728a9333753610124bfaea12af1123b0e247fbb39b2b6b13fe34484  original_kernel_DR590W.img.sue
35ce0f42e728a9333753610124bfaea12af1123b0e247fbb39b2b6b13fe34484  generated_kernel_DR590W.img.sue
```

## Requirements
* Python 3

## Usage
```
$ ./sue_checksum.py image.img image.img.sue
```

## License
MIT