def curvature_hist(img, step=10, plot=False):
    cvt = curvature(img, step=step)

    nbins = 10
    vmin = 0
    vmax = 0.4
    bins = np.linspace(vmin, vmax, nbins + 1, endpoint=True)
    h, _ = np.histogram(cvt, bins=bins, range=(vmin, vmax))
    h = h / float(len(cvt))

    if plot:
        pl.title('histogram of curvatures')
        pl.bar(bins[:-1], h, width=0.02, align='center')
        pl.xlim((bins[0], bins[-1]))

    return h