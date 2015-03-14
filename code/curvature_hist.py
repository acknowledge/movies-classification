def curvature_hist(img, step=10, plot=False):
    gs = gridspec.GridSpec(2,2)
    cvt = curvature(img, step, plot, gs)
    pl.subplot(gs[1, :])
    pl.hist(cvt)
    pl.title("histogram of curvatures")
    return cvt