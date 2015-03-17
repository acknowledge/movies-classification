def curvature_hist(img, step=10, plot=False):
    n = 10
    gs = gridspec.GridSpec(2,2)
    cvt = curvature(img, step, plot, gs)
    
    min = 0
    max = 0.4
    qty = cvt.size
    bin_size = (max-min)/n
    
    #binsPos = np.arange(0, 0.41, 0.04)
    binsPos = np.linspace(min, max, 11)
    binsVal, binsPos = np.histogram(cvt, binsPos)
    binsVal = binsVal / float(len(cvt))
        
    if plot:
        pl.subplot(gs[1, :])

        pl.bar(binsPos[:-1], binsVal, 0.02)
        pl.xlim((min, max))
        pl.title("histogram of curvatures")

    return np.array(binsVal)