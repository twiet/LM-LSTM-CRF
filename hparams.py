class hparams:
    checkpoint_dir = "./checkpoint/"
    load_check_point = False
    rand_embedding = False
    gpu = 0
    batch_size = 10
    unk = "unk"
    char_hidden = 300
    word_hidden = 300
    drop_out = 0.55
    epoch = 200
    start_epoch = 0
    caseless = True
    char_dim = 30
    word_dim = 100
    char_layers = 1
    word_layers = 1
    lr = 0.015
    lr_decay = 0.05
    fine_tune = False
    load_opt = True
    update = "sgd"
    momentum = 0.9
    clip_grad = 5
    small_crf = True
    mini_count = 5
    lambda0 = 1
    co_train = True
    patience = 15
    high_way = True
    highway_layers = 1
    eva_matrix = "fa"
    least_iters = 50
    shrink_embedding = True
    decode_type = "label"