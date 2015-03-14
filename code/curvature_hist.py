def curvature_hist(img, step=10, plot=False):
    n = 10
    gs = gridspec.GridSpec(2,2)
    cvt = curvature(img, step, plot, gs)
    
    if plot:
        pl.subplot(gs[1, :])
        pl.hist(cvt)
        pl.title("histogram of curvatures")
        
    min = cvt.min()
    max = cvt.max()
    qty = cvt.size
    bin_size = (max-min)/n
    
    bins = [0] * n

    for i in range(0,n):
        for e in cvt:
            if e >= min+(i*bin_size):
                if e < min+((i+1)*bin_size):
                    bins[i] = bins[i]+1
    for i in range(0,n):
        bins[i] = bins[i]*1.0/qty

    return bins