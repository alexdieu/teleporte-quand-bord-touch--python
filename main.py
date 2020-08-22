import pygame

#To do : ajouter un menu configurable
hauteur = 800
largeur = 800
FPS = 60

#couleurs du jeu (Complété):
blanc = (255,255,255)
bleu = (0,0,255)
vert = (0,255,0)
rouge = (255,0,0)
noir = (0,0,0)
orange = (255,100,10)
jaune = (255,255,0)
bleu_vert = (0,255,170)
marron = (115,0,0)
vert_clair = (180,255,100)
rose = (255,100,180)
violet = (240,0,255)
gris = (127,127,127)
magenta = (255,0,230)
marron_fonce = (100,40,0)
vert_foret = (0,50,0)
bleu_natif = (0,0,100)
terre = (210,150,75)
bleu_ciel = (0,255,255)
gris_clair = (200,200,200)
gris_sombre = (50,50,50)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("ESSAI 5")
clock = pygame.time.Clock()

class Joueur(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(vert)
        self.rect = self.image.get_rect()
        self.rect.center = (hauteur / 2, largeur / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > largeur:
            self.rect.right = 0


tousprites = pygame.sprite.Group()
joueur = Joueur()
tousprites.add(joueur)

marche = True
while marche:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            marche = False
    screen.fill(noir)
    tousprites.draw(screen)
    tousprites.update()
    pygame.display.flip()
