def recur_mult(mcand,mplier):
    if mplier == 1:
        return mcand
    else:
        return mcand + recur_mult(mcand,mplier-1)
print(recur_mult(25,0))