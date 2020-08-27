class ImageSizeOptions(object):
    IMAGE_HEIGHT = 20
    IMAGE_CHANNEL_HEIGHT = 20
    IMAGE_CHANNELS = 1
    SEQ_LENGTH = 1000
    SEQ_OVERLAP = 50
    LABEL_LENGTH = SEQ_LENGTH

    TOTAL_LABELS = 5
    MIN_SEQUENCE_LENGTH = 1000
    MIN_IMAGE_OVERLAP = 100


class ReadFilterOptions(object):
    MIN_MAPQ = 1
    MIN_BASEQ = 0
    INCLUDE_SUPPLEMENTARY = False


class CandidateFinderOptions(object):
    ALLELE_FREQ_THRESHOLD = 0.00

    SNP_ALT_FREQ_COEF = 0
    SNP_NON_REF_PROB_COEF = 0.000214
    SNP_ALLELE_WEIGHT_COEF = 0.994386
    SNP_BIAS_TERM = -1.8e-05
    SNP_THRESHOLD = 0.001
    SNP_FREQ_THRESHOLD = 0.10
    SNP_UPPER_FREQ = 0.5

    INSERT_ALT_FREQ_COEF = 0
    INSERT_NON_REF_PROB_COEF = 0.615082
    INSERT_ALLELE_WEIGHT_COEF = 0.523549
    INSERT_BIAS_TERM = 0.015388
    INSERT_THRESHOLD = 0.02
    IN_FREQ_THRESHOLD = 0.20
    IN_UPPER_FREQ = 0.5

    DELETE_ALT_FREQ_COEF = 0
    DELETE_NON_REF_PROB_COEF = 0.450943
    DELETE_ALLELE_WEIGHT_COEF = 0.136223
    DELETE_BIAS_TERM = 1.3e-05
    DELETE_THRESHOLD = 0.01
    DEL_FREQ_THRESHOLD = 0.20
    DEL_UPPER_FREQ = 0.5

    SAFE_BASES = 20
    ALT_PROB_THRESHOLD = 0.01


class TrainOptions(object):
    # these two parameters are important, make sure you are sliding in a way that you cover the full sequence length
    # the training loop breaks when current_index + TRAIN_WINDOW > LAST_INDEX. You may lose information if you don't
    # slide correctly
    TRAIN_WINDOW = 100
    WINDOW_JUMP = 50
    GRU_LAYERS = 1
    HIDDEN_SIZE = 128


class AlingerOptions(object):
    # base and map quality
    ALIGNMENT_SAFE_BASES = 20
    MIN_MAP_QUALITY = 20

    MAX_READS_IN_REGION = 1500
    RANDOM_SEED = 2719747673

