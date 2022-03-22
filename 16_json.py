import json

class Midconf():
    def __init__(self):
        self.H_eval = 256
        self.W_eval = 256
        self.batchsize = 4
        self.shuffle = True
        self.num_workers = 0
        self.epochs=20
        self.pix_batch=256

netconf = {
        "dims": [256, 256, 256, 256, 256, 256, 256, 256],
        "dropout": [0, 1, 2, 3, 4, 5, 6, 7],
        "dropout_prob": 0.2,
        "norm_layers": [0, 1, 2, 3, 4, 5, 6, 7],
        "latent_in": [4],
        "uvs_in_all": False,
        "use_tanh": False,
        "latent_dropout": False,
        "weight_norm": True,
    }

conf2={'dfa':432,'daf':23}
netconf.update(conf2)
print(netconf)
# with open('temp.json','w') as fileobj:
#     json.dump(netconf,fileobj)

