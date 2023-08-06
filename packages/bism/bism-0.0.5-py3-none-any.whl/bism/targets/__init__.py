from bism.targets.affinities import affinities
from bism.targets.local_shape_descriptors import lsd
from bism.targets.mtlsd import mtlsd

_valid_targets = {
    'lsd': lsd,
    'affinities': affinities,
    'mtlsd': mtlsd

}