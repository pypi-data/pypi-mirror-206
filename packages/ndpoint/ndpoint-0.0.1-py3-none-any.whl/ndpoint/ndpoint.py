import math
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from PIL import Image

# Spectrum表示の画像サイズ
# 本当はサンプル数に合わせてサイズを変えなければいけないが、
# 利便性を取ってユーザー設定できるように。
SPECTRUM_IMAGE_SIZE = 256
#
def computePowerSpectrum2d(samples, f, d0, d1, numSpectrumSample):
    ds = 2.0 * math.pi * (f[0] * samples[d0][:numSpectrumSample] + f[1] * samples[d1][:numSpectrumSample])
    st = np.sum(np.sin(ds))
    ct = np.sum(np.cos(ds))
    return (st * st + ct * ct) / numSpectrumSample

# TODO: 高速化
def drawPowerSpectrum(samples, d0, d1, numSpectrumSample):
    #img = Image.new('RGB', (SPECTRUM_IMAGE_SIZE,SPECTRUM_IMAGE_SIZE))
    #pixels = img.load() 
    pixels = []
    for y in range(SPECTRUM_IMAGE_SIZE):
        line = []
        for x in range(SPECTRUM_IMAGE_SIZE):
            f = [
                (x/SPECTRUM_IMAGE_SIZE-0.5) * 2.0 * SPECTRUM_IMAGE_SIZE,
                (y/SPECTRUM_IMAGE_SIZE-0.5) * 2.0 * SPECTRUM_IMAGE_SIZE
                ]
            pv = computePowerSpectrum2d(samples, f, d0, d1, numSpectrumSample)
            # tone mapping
            pvi = int(math.log2(pv + 0.25) * 255)
            line.append(pvi)
            #pixels[x,y] = (pvi, pvi, pvi)
        pixels.append(line)
    return pixels

def plot(samples, 
         numPlotSample = None,
         numSpectrumSample = None,
         dmin=None, 
         dmax=None,
         title=None, 
         pointScale=1.0, 
         spectrum=False,
         subPlotSize=12.0,
         progress = True,
         enableLabel=False):
    """plot sample points
    Parameters:
    ----------
    sample : TODO: DxNのサンプル集合であることを明示する
        TODO: 多重配列であればnumpyでも良い旨をかく
    numPlotSample : int
        #plot sample
    dmin : int
        maximum dimension
    dmax : int
        maximum dimension
    plotSizeScale : float
        size of plot point radius scale
    title : string
        title of figure
    spectrum : bool
        enable spectrum plot

    Returns:
    ----------
    int
        sum of x and y
    """
    # 次元とサンプル数
    # TODO: これを最初に収集しないようにする
    numDim    = len(samples)
    numSample = len(samples[0])

    if dmax != None:
        numDim = dmax
    # 必要な次元のリストを全て列挙する
    dims = []
    for d0 in range(numDim-1):
        for d1 in range(d0+1, numDim):
            dims.append([d0,d1])

    # ポイントサイズの算出
    # ポイント数がx100になったら1/10の半径にする
    BASE_POINT_SIZE = 300.0
    pointSize = pointScale * BASE_POINT_SIZE / (math.sqrt(numPlotSample) * numDim)
    print(pointSize)
    
    figsize = (subPlotSize * (numDim+1)/numDim, subPlotSize) if spectrum else (subPlotSize, subPlotSize)
    fig = plt.figure(figsize=figsize)
    # 
    for dim in tqdm(dims, disable = not progress):
        d0 = dim[0]
        d1 = dim[1]
        hcol = (numDim+1) if spectrum else numDim
        axPlot = fig.add_subplot(numDim, hcol, d0 + 1 + (d1-1) * hcol)

        # [0,1]に限定する
        axPlot.set_xlim(0,1)
        axPlot.set_ylim(0,1)
        #
        major_ticks = np.arange(0, 1, 1/4)
        axPlot.set_xticks(major_ticks)
        axPlot.set_yticks(major_ticks)
        axPlot.grid(which='both')
        axPlot.tick_params(
            labelleft=False, labelbottom=False,
            bottom=False, left=False,right=False,top=False)
        axPlot.set_aspect('equal', 'box')
        # label
        if enableLabel:
            if d0 == 0:
                axPlot.set_ylabel(str(d1+1))
            if d1 == numDim-1:
                axPlot.set_xlabel(str(d0+1))

        # プロット時の最大のサンプル数
        if numPlotSample == None:
            numPlotSample = numSample
        axPlot.scatter(samples[d0][:numPlotSample], samples[d1][:numPlotSample], c=range(numPlotSample), s=pointSize, cmap="viridis")
        #
        if spectrum:
            axPower = fig.add_subplot(numDim, numDim+1, d1 + 1 + d0 * (numDim+1))
            axPower.tick_params(
                labelleft=False, labelbottom=False,
                bottom=False, left=False,right=False,top=False)
            if enableLabel:
                if d0 == 0:
                    axPower.xaxis.set_label_position("top")
                    axPower.set_xlabel(str(d1+1))
                if d1 == numDim-1:
                    axPower.yaxis.set_label_position("right")
                    axPower.set_ylabel(str(d0+1))

            if numSpectrumSample == None:
                numSpectrumSample = numSample
            img = drawPowerSpectrum(samples, d0, d1, numSpectrumSample)
            axPower.pcolorfast(img, cmap="Greys")
    
    # setting title. Commented out because it doesn't work properly...
    #if title != None: plt.suptitle(title,x=0.5, ha='center')
    
    plt.tight_layout() 
    plt.show()

