import torch
from PIL import Image
from torchvision.transforms import functional as F


class ResizePad(torch.nn.Module):
    """Resize the input image to the given size.
    The image can be a PIL Image or a torch Tensor, in which case it is expected
    to have [..., H, W] shape, where ... means an arbitrary number of leading dimensions

    Args:
        size (sequence or int): Desired output size. If size is a sequence like
            (h, w), output size will be matched to this. If size is an int,
            smaller edge of the image will be matched to this number.
            i.e, if height > width, then image will be rescaled to
            (size * height / width, size).
            In torchscript mode padding as single int is not supported, use a tuple or
            list of length 1: ``[size, ]``.
        interpolation (int, optional): Desired interpolation enum defined by `filters`_.
            Default is ``PIL.Image.BILINEAR``. If input is Tensor, only ``PIL.Image.NEAREST``, ``PIL.Image.BILINEAR``
            and ``PIL.Image.BICUBIC`` are supported.
    """

    def __init__(self, side_size, interpolation=Image.BILINEAR):
        super().__init__()
        if not isinstance(side_size, int):
            raise TypeError('Size should be int')
        self.side_size = side_size
        self.interpolation = interpolation

    def forward(self, img):
        """
        Args:
            img (PIL Image or Tensor): Image to be scaled.

        Returns:
            PIL Image or Tensor: Rescaled image.
        """
        h, w = 0, 0
        if isinstance(img, Image.Image):
            w, h = img.size
        elif isinstance(img, torch.Tensor):
            size = img.size()
            if len(size) == 4:
                raise ValueError('batch image is not support')
            elif len(size) == 3:
                c, h, w = img
            elif len(size) == 2:
                h, w = img
            else:
                raise ValueError('incorrect image data')
        pad = [0, 0, 0, 0]
        if h > w:
            new_h = self.side_size
            new_w = int(w * new_h / h)
            pad[0] = int((self.side_size - new_w) / 2)  # pad left
            pad[2] = self.side_size - pad[0] - new_w    # pad right
        else:
            new_w = self.side_size
            new_h = int(h * new_w / w)
            pad[1] = int((self.side_size - new_h) / 2)  # pad top
            pad[3] = self.side_size - pad[1] - new_h    # pad bottom
        img = F.resize(img, [new_h, new_w], self.interpolation)
        img = F.pad(img, pad, padding_mode='constant')
        return img


if __name__ == "__main__":

    img_test = Image.open('1.jpg')
    resize_pad = ResizePad(side_size=224)
    img_transformed = resize_pad(img_test)
    print(img_transformed.size)
    img_transformed.show()