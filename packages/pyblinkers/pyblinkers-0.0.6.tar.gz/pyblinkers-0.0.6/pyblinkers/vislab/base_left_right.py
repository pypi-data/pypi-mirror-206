import numpy as np

from pyblinkers.utilities.zero_crossing import (_maxPosVelFrame, _get_left_base, _get_right_base)


def create_left_right_base_vislab(data,df):
    blinkVelocity = np.diff(data, axis=0)
    df = df.dropna()
    df[['maxPosVelFrame', 'maxNegVelFrame']] = df.apply(
        lambda x: _maxPosVelFrame(blinkVelocity, x['maxFrames'], x['leftZero'],
                                  x['rightZero']), axis=1, result_type="expand")

    ## Lets check some condition especially for data with anamoly

    df = df[df['outerStarts'] < df['maxPosVelFrame']]  # Filter and take only row that normal
    df['leftBase'] = df.apply(lambda x: _get_left_base(blinkVelocity, x['outerStarts'], x['maxPosVelFrame']), axis=1)

    df = df.dropna()

    df['rightBase'] = df.apply(lambda x: _get_right_base(data, blinkVelocity, x['outerEnds'], x['maxNegVelFrame']),
                               axis=1)
    return df