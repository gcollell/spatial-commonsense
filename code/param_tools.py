def get_default_params(model_type):
    # Get default parameters

    par_learning = {}
    par_learning['batch_size'] = 64
    par_learning['LR'] = 0.0001 # learning rate
    par_learning['activation'] = 'relu' # OPTIONS=('sigmoid','softmax', 'linear', 'tanh' or 'relu', 'elu' or 'softplus')
    par_learning['n_epochs'] = 10
    par_learning['n_hidden'] = 100
    par_learning['n_layers'] = 2
    par_learning['emb_initialize'] = 'emb' # OPTIONS: 'emb' , 'uniform'

    if model_type == 'REG':
        par_learning['loss'] = 'mse'
        par_learning['metrics'] = ['mse']
        par_learning['output_acti'] = 'linear'

    if model_type == 'PIX':
        par_learning['loss'] = 'binary_crossentropy'
        par_learning['metrics'] = ['binary_crossentropy', 'mse']
        par_learning['output_acti'] = 'sigmoid'

    return par_learning
















