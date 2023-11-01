import numpy as np
import numpy.typing as npt

def apply2DConvolutionOnChannel(imgChannel: npt.NDArray, kernel: npt.NDArray, stride: int = 1, padding: int = 0):

    # assuming padding is 0 and string is 1

    h, w = imgChannel.shape
    kh, kw = kernel.shape
    assert kh % 2 != 0 
    assert kw %2 != 0
    output = np.zeros((h, w), dtype=np.int16)
    offsetY = kh // 2
    offsetX = kw // 2
    for y in range(offsetY, h-offsetY):
        for x in range(offsetX, w-offsetX):
            imgArea = imgChannel[y-offsetY : y+offsetY+1, x-offsetX : x+offsetX+1]
            pixelVal = np.sum(kernel * imgArea)
            output[y, x] = int(pixelVal)
            # return output

    return output

def apply2DConvolution(img: npt.NDArray, kernel: npt.NDArray, stride: int = 1, padding: int = 0):
    if img.shape[-1] == 3:
        r = img1[:, :, 0]
        g = img1[:, :, 1]
        b = img1[:, :, 2]
        return np.stack([
            apply2DConvolutionOnChannel(r, kernel),
            apply2DConvolutionOnChannel(g, kernel),
            apply2DConvolutionOnChannel(b, kernel),
        ], axis=-1)


    

def juxtapose(img1: npt.NDArray, img2: npt.NDArray):
    fig, axes = plt.subplots(1, 2)
    axes[0].imshow(img1)
    axes[1].imshow(img2)
    plt.show()