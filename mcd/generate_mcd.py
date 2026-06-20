# -*- coding: utf-8 -*-
"""Generateur d'un MCD lisible pour ZandoMarketPlace.

Le diagramme Mocodo original entasse 23 entites + 27 associations sur 4 colonnes
de 636px de large : les deux entites-pivots (UTILISATEUR, PRODUIT) ont chacune
8 a 11 relations qui partent dans toutes les directions sous forme de lignes
diagonales qui traversent toutes les autres boites. Resultat illisible.

Ce script redessine le meme contenu (memes entites, attributs, associations,
cardinalites - rien n'est invente) avec un routage en "bus" :
- UTILISATEUR et PRODUIT sont des hubs verticaux centraux
- leurs relations distantes descendent d'abord dans un couloir horizontal
  vide (la "gouttiere"), puis plongent dans un couloir vertical reserve a
  cote de chaque colonne, avant de rentrer dans la bonne boite par un
  court coude horizontal. Aucune ligne ne traverse jamais une autre boite.
"""
import html

FONT_TITLE = 16
FONT_ATTR = 13
FONT_LABEL = 13
CHAR_W_TITLE = 8.6
CHAR_W_ATTR = 7.1
PAD_X = 12
LINE_H = 20
TITLE_H = 30

STROKE = "#1f2233"
HUB_COLOR = "#7b5cff"
PROD_COLOR = "#f72585"
LOCAL_COLOR = "#1f2233"
LATERAL_COLOR = "#0a8f6b"
BG = "#ffffff"
BOX_FILL = "#ffffff"
BOX_TITLE_FILL = "#eef0fb"


def text_width(s, char_w):
    return len(s) * char_w


class Entity:
    def __init__(self, name, attrs):
        self.name = name
        self.attrs = attrs  # list of attribute labels, first = identifiant
        self.cx = 0
        self.cy = 0
        self.w = 0
        self.h = 0

    def compute_size(self):
        title_w = text_width(self.name, CHAR_W_TITLE) + 2 * PAD_X
        attr_w = max([text_width(a, CHAR_W_ATTR) for a in self.attrs] + [0]) + 2 * PAD_X
        self.w = max(title_w, attr_w, 120)
        self.h = TITLE_H + LINE_H * len(self.attrs) + 10

    @property
    def left(self):
        return self.cx - self.w / 2

    @property
    def right(self):
        return self.cx + self.w / 2

    @property
    def top(self):
        return self.cy - self.h / 2

    @property
    def bottom(self):
        return self.cy + self.h / 2

    def svg(self):
        x, y = self.left, self.top
        out = []
        out.append(f'<g class="entity">')
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{self.w:.1f}" height="{self.h:.1f}" fill="{BOX_FILL}" stroke="{STROKE}" stroke-width="1.6" rx="3"/>')
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{self.w:.1f}" height="{TITLE_H:.1f}" fill="{BOX_TITLE_FILL}" stroke="{STROKE}" stroke-width="1.6" rx="3"/>')
        out.append(f'<text x="{self.cx:.1f}" y="{y + TITLE_H/2 + 5:.1f}" text-anchor="middle" font-family="Segoe UI, Verdana" font-size="{FONT_TITLE}" font-weight="700" fill="{STROKE}">{html.escape(self.name)}</text>')
        for i, a in enumerate(self.attrs):
            ay = y + TITLE_H + LINE_H * i + 15
            weight = "700" if i == 0 else "400"
            deco = ' text-decoration="underline"' if i == 0 else ""
            out.append(f'<text x="{x + PAD_X:.1f}" y="{ay:.1f}" font-family="Segoe UI, Verdana" font-size="{FONT_ATTR}" font-weight="{weight}"{deco} fill="#3a3d5c">{html.escape(a)}</text>')
            if i == 0 and len(self.attrs) > 1:
                out.append(f'<line x1="{x:.1f}" y1="{y + TITLE_H + LINE_H - 5:.1f}" x2="{x + self.w:.1f}" y2="{y + TITLE_H + LINE_H - 5:.1f}" stroke="{STROKE}" stroke-width="0.8" stroke-dasharray="2,2"/>')
        out.append('</g>')
        return "\n".join(out)


def diamond_svg(cx, cy, label, color):
    w = text_width(label, 6.6) + 22
    h = 30
    x, y = cx - w / 2, cy - h / 2
    return (
        f'<g class="assoc">'
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="14" fill="#ffffff" stroke="{color}" stroke-width="1.6"/>'
        f'<text x="{cx:.1f}" y="{cy + 4:.1f}" text-anchor="middle" font-family="Segoe UI, Verdana" font-size="11.5" font-weight="700" fill="{color}">{html.escape(label)}</text>'
        f'</g>'
    ), w, h


def card_label(x, y, text, anchor="middle", color="#3a3d5c"):
    return f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}" font-family="Verdana" font-size="{FONT_LABEL}" font-weight="700" fill="{color}">{html.escape(text)}</text>'


# ---------------------------------------------------------------------------
# DONNEES (reprises telles quelles de mcd/zandomarketplace.mcd)
# ---------------------------------------------------------------------------

ENTITIES = {
    "UTILISATEUR": ["identifiant", "nom utilisateur", "email", "type utilisateur", "téléphone", "pays", "ville"],
    "PROFIL_CLIENT": ["adresse", "points fidélité"],
    "PROFIL_VENDEUR": ["nom commercial", "email pro", "vérifié"],
    "PROFIL_ADMIN": ["gère utilisateurs", "gère paiements"],
    "CATEGORIE": ["nom catégorie", "slug catégorie", "actif", "quotidien"],
    "COULEUR": ["nom couleur", "code hexa"],
    "TAILLE": ["nom taille"],
    "PRODUIT": ["titre", "slug produit", "prix", "devise", "remise %", "stock", "approuvé"],
    "VARIANTE": ["prix variante", "remise variante", "stock variante"],
    "IMAGE_VARIANTE": ["image variante"],
    "PRODUIT_NUMERIQUE": ["fichier", "clé licence"],
    "PUBLICITE": ["titre pub", "priorité pub", "clics", "vues pub"],
    "IMAGE_PRODUIT": ["image produit", "principale"],
    "AVIS": ["note", "aimé"],
    "LISTE_SOUHAITS": ["créée le"],
    "ARTICLE_SOUHAIT": ["ajouté le"],
    "VUE_PRODUIT": ["vu le"],
    "PANIER": ["créé le"],
    "ARTICLE_PANIER": ["quantité panier"],
    "COMMANDE": ["total", "statut", "adresse livraison"],
    "LIGNE_COMMANDE": ["prix ligne", "quantité ligne"],
    "PAIEMENT": ["montant", "méthode", "réussi"],
    "CAROUSEL": ["titre slide", "priorité slide", "actif slide"],
}

# (nom, cardinalite_a, entite_a, cardinalite_b, entite_b, type)
# type: header / hubhub / hubU / hubP / local / lateral / selfloop
RELATIONS = [
    ("A_PROFIL_CLIENT", "1,1", "UTILISATEUR", "1,1", "PROFIL_CLIENT", "header"),
    ("A_PROFIL_VENDEUR", "1,1", "UTILISATEUR", "1,1", "PROFIL_VENDEUR", "header"),
    ("A_PROFIL_ADMIN", "1,1", "UTILISATEUR", "1,1", "PROFIL_ADMIN", "header"),
    ("POSSEDE", "0,N", "PRODUIT", "1,1", "UTILISATEUR", "hubhub"),
    ("SE_DECLINE_EN", "0,N", "CATEGORIE", "0,1", "CATEGORIE", "selfloop"),
    ("CLASSE_DANS", "0,N", "PRODUIT", "0,1", "CATEGORIE", "hubP"),
    ("DECLINE", "1,N", "VARIANTE", "1,1", "PRODUIT", "hubP"),
    ("COLOREE", "0,N", "VARIANTE", "0,1", "COULEUR", "lateral"),
    ("TAILLEE", "0,N", "VARIANTE", "0,1", "TAILLE", "lateral"),
    ("ILLUSTRE_VARIANTE", "1,N", "IMAGE_VARIANTE", "1,1", "VARIANTE", "local"),
    ("EST_VERSION_NUM", "1,1", "PRODUIT_NUMERIQUE", "1,1", "PRODUIT", "hubP"),
    ("PROMEUT", "1,N", "PUBLICITE", "1,1", "PRODUIT", "hubP"),
    ("ILLUSTRE_PRODUIT", "1,N", "IMAGE_PRODUIT", "1,1", "PRODUIT", "hubP"),
    ("EVALUE", "0,N", "AVIS", "1,1", "PRODUIT", "hubP"),
    ("REDIGE", "0,N", "AVIS", "1,1", "UTILISATEUR", "hubU"),
    ("A_WISHLIST", "1,1", "UTILISATEUR", "1,1", "LISTE_SOUHAITS", "hubU"),
    ("CONTIENT_SOUHAIT", "0,N", "ARTICLE_SOUHAIT", "1,1", "LISTE_SOUHAITS", "local"),
    ("SOUHAITE", "0,N", "ARTICLE_SOUHAIT", "1,1", "PRODUIT", "hubP"),
    ("CONSULTE", "0,N", "VUE_PRODUIT", "1,1", "UTILISATEUR", "hubU"),
    ("EST_CONSULTE", "0,N", "VUE_PRODUIT", "1,1", "PRODUIT", "hubP"),
    ("A_PANIER", "0,N", "PANIER", "0,1", "UTILISATEUR", "hubU"),
    ("DANS_PANIER", "0,N", "ARTICLE_PANIER", "1,1", "PANIER", "local"),
    ("AJOUTE_AU_PANIER", "0,N", "ARTICLE_PANIER", "1,1", "PRODUIT", "hubP"),
    ("PASSE", "0,N", "COMMANDE", "0,1", "UTILISATEUR", "hubU"),
    ("DANS_COMMANDE", "0,N", "LIGNE_COMMANDE", "1,1", "COMMANDE", "local"),
    ("REFERE_PRODUIT", "0,N", "LIGNE_COMMANDE", "0,1", "PRODUIT", "hubP"),
    ("REGLE", "0,N", "PAIEMENT", "0,1", "UTILISATEUR", "hubU"),
]

COLUMNS = [
    ("Catalogue", ["CATEGORIE", "COULEUR", "TAILLE"]),
    ("Variantes & medias", ["VARIANTE", "IMAGE_VARIANTE", "PRODUIT_NUMERIQUE", "PUBLICITE", "IMAGE_PRODUIT"]),
    ("Engagement", ["AVIS", "LISTE_SOUHAITS", "ARTICLE_SOUHAIT", "VUE_PRODUIT"]),
    ("Panier & commande", ["PANIER", "ARTICLE_PANIER", "COMMANDE", "LIGNE_COMMANDE", "PAIEMENT"]),
    ("Marketing", ["CAROUSEL"]),
]

LOCAL_PAIRS = {
    ("VARIANTE", "IMAGE_VARIANTE"),
    ("LISTE_SOUHAITS", "ARTICLE_SOUHAIT"),
    ("PANIER", "ARTICLE_PANIER"),
    ("COMMANDE", "LIGNE_COMMANDE"),
}

ROW_GAP = 95
CORRIDOR_GAP = 100
MARGIN = 50


def build():
    ents = {name: Entity(name, attrs) for name, attrs in ENTITIES.items()}
    for e in ents.values():
        e.compute_size()

    # --- colonnes : largeur = max largeur de boite du groupe ---
    col_w = {}
    for cname, members in COLUMNS:
        col_w[cname] = max(ents[m].w for m in members)
    hub_w = max(ents["UTILISATEUR"].w, ents["PRODUIT"].w)

    order = ["Catalogue", "HUB", "Variantes & medias", "Engagement", "Panier & commande", "Marketing"]
    widths = {**col_w, "HUB": hub_w}

    x_cursor = MARGIN
    col_x = {}
    for i, cname in enumerate(order):
        w = widths[cname]
        if i == 0:
            x_cursor += w / 2
        else:
            x_cursor += CORRIDOR_GAP * 2 + 40 + w / 2
        col_x[cname] = x_cursor
        x_cursor += w / 2

    hub_x = col_x["HUB"]

    # --- bandeau haut : UTILISATEUR + 3 profils ---
    # decales pour qu'aucun profil ni son losange ne retombe sur l'axe hub_x
    # (l'epine verticale UTILISATEUR-PRODUIT-bus occupe cet axe sur toute la hauteur)
    ents["UTILISATEUR"].cx = hub_x
    ents["UTILISATEUR"].cy = MARGIN + ents["UTILISATEUR"].h / 2
    profile_y = ents["UTILISATEUR"].bottom + 110
    ents["PROFIL_CLIENT"].cx, ents["PROFIL_CLIENT"].cy = hub_x - 520, profile_y
    ents["PROFIL_VENDEUR"].cx, ents["PROFIL_VENDEUR"].cy = hub_x - 200, profile_y
    ents["PROFIL_ADMIN"].cx, ents["PROFIL_ADMIN"].cy = hub_x + 340, profile_y

    trunk_u_y = max(ents["PROFIL_CLIENT"].bottom, ents["PROFIL_VENDEUR"].bottom, ents["PROFIL_ADMIN"].bottom) + 45
    ents["PRODUIT"].cx = hub_x
    ents["PRODUIT"].cy = trunk_u_y + 50 + ents["PRODUIT"].h / 2
    trunk_p_y = ents["PRODUIT"].bottom + 40
    trunk_l_y = trunk_p_y + 35
    grid_top = trunk_l_y + 55

    # --- grille des colonnes domaine ---
    for cname, members in COLUMNS:
        y = grid_top
        for m in members:
            e = ents[m]
            e.cx = col_x[cname]
            e.cy = y + e.h / 2
            y += e.h + ROW_GAP

    # --- normalisation : personne ne doit deborder a gauche (ex: PROFIL_CLIENT decale) ---
    min_left = min(e.left for e in ents.values())
    if min_left < MARGIN:
        shift = MARGIN - min_left
        for e in ents.values():
            e.cx += shift
        hub_x += shift
        col_x = {k: v + shift for k, v in col_x.items()}

    return ents, col_x, hub_x, trunk_u_y, trunk_p_y, trunk_l_y, grid_top


def bus_path(x_src, y_src, trunk_y, target, side):
    if side == "left":
        x_entry = target.left
        x_corr = x_entry - CORRIDOR_GAP
    else:
        x_entry = target.right
        x_corr = x_entry + CORRIDOR_GAP
    d = (f"M {x_src:.1f} {y_src:.1f} L {x_src:.1f} {trunk_y:.1f} "
         f"L {x_corr:.1f} {trunk_y:.1f} L {x_corr:.1f} {target.cy:.1f} L {x_entry:.1f} {target.cy:.1f}")
    return d, x_corr


def render(ents, col_x, hub_x, trunk_u_y, trunk_p_y, trunk_l_y, grid_top):
    svg = []
    hubU_i, hubP_i = 0, 0
    n_hubU = sum(1 for r in RELATIONS if r[5] == "hubU")
    n_hubP = sum(1 for r in RELATIONS if r[5] == "hubP")
    target_offsets = {}  # entity name -> count of incoming bus lines seen so far

    def stagger(name, dy=13):
        n = target_offsets.get(name, 0)
        target_offsets[name] = n + 1
        return (n - 0.5) * dy

    for name, card_a, ea, card_b, eb, kind in RELATIONS:
        A, B = ents[ea], ents[eb]

        if kind == "header":
            x1, y1 = A.cx, A.bottom
            x2, y2 = B.cx, B.top
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            svg.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{LOCAL_COLOR}" stroke-width="1.4"/>')
            d, w, h = diamond_svg(mx, my, name, HUB_COLOR)
            svg.append(d)
            svg.append(card_label(x1 + (mx - x1) * 0.35, y1 + (my - y1) * 0.35 - 6, card_a))
            svg.append(card_label(x2 + (mx - x2) * 0.35, y2 + (my - y2) * 0.35 - 6, card_b))

        elif kind == "hubhub":
            top_e, top_c, bot_e, bot_c = (A, card_a, B, card_b) if A.cy < B.cy else (B, card_b, A, card_a)
            x = top_e.cx
            y1, y2 = top_e.bottom, bot_e.top
            my = (y1 + y2) / 2
            svg.append(f'<line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}" stroke="{PROD_COLOR}" stroke-width="2"/>')
            d, w, h = diamond_svg(x, my, name, PROD_COLOR)
            svg.append(d)
            svg.append(card_label(x + 38, y1 + 14, top_c))
            svg.append(card_label(x + 38, y2 - 10, bot_c))

        elif kind == "selfloop":
            x, y = A.left, A.cy
            d = f"M {x:.1f} {y-26:.1f} C {x-70:.1f} {y-40:.1f} {x-70:.1f} {y+40:.1f} {x:.1f} {y+26:.1f}"
            svg.append(f'<path d="{d}" fill="none" stroke="{LOCAL_COLOR}" stroke-width="1.4"/>')
            dd, w, h = diamond_svg(x - 78, y, name, LOCAL_COLOR)
            svg.append(dd)
            svg.append(card_label(x - 20, y - 32, "sous-categorie 0,N", anchor="end"))
            svg.append(card_label(x - 20, y + 40, "categorie mere 0,1", anchor="end"))

        elif kind == "local":
            top_e, top_c, bot_e, bot_c = (A, card_a, B, card_b) if A.cy < B.cy else (B, card_b, A, card_a)
            x = top_e.cx
            y1, y2 = top_e.bottom, bot_e.top
            my = (y1 + y2) / 2
            svg.append(f'<line x1="{x:.1f}" y1="{y1:.1f}" x2="{x:.1f}" y2="{y2:.1f}" stroke="{LOCAL_COLOR}" stroke-width="1.4"/>')
            d, w, h = diamond_svg(x, my, name, LOCAL_COLOR)
            svg.append(d)
            svg.append(card_label(x + 34, y1 + 14, top_c))
            svg.append(card_label(x + 34, y2 - 10, bot_c))

        elif kind in ("hubU", "hubP", "lateral"):
            if kind == "hubU":
                hub_ent, hub_name, trunk_y, color = ents["UTILISATEUR"], "UTILISATEUR", trunk_u_y, HUB_COLOR
                x_src, y_src = hub_ent.cx, hub_ent.bottom
            elif kind == "hubP":
                hub_ent, hub_name, trunk_y, color = ents["PRODUIT"], "PRODUIT", trunk_p_y, PROD_COLOR
                x_src, y_src = hub_ent.cx, hub_ent.bottom
            else:
                hub_ent, hub_name, trunk_y, color = ents["VARIANTE"], "VARIANTE", trunk_l_y, LATERAL_COLOR
                x_src, y_src = hub_ent.left, hub_ent.cy + stagger("VARIANTE_OUT", 18)

            other, other_is_a = (B, False) if ea == hub_name else (A, True)
            hub_card = card_a if ea == hub_name else card_b
            other_card = card_b if ea == hub_name else card_a

            side = "left" if other.cx > hub_ent.cx else "right"
            d, x_corr = bus_path(x_src, y_src, trunk_y, other, side)
            svg.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.4" opacity="0.85"/>')

            # le losange reste DANS le couloir (jamais au-dessus de la boite cible)
            dy = stagger(ea + eb)
            dxm, dym = x_corr, other.cy + dy
            dd, w, h = diamond_svg(dxm, dym, name, color)
            svg.append(dd)

            # les deux cardinalites se lisent l'une au-dessus, l'autre au-dessous du losange
            svg.append(card_label(dxm, dym - h / 2 - 8, hub_card, color=color))
            svg.append(card_label(dxm, dym + h / 2 + 16, other_card, color=color))

    return svg


def legend(x, y):
    items = [
        (HUB_COLOR, "Bus UTILISATEUR (relations distantes)"),
        (PROD_COLOR, "Bus PRODUIT (relations distantes)"),
        (LATERAL_COLOR, "Relation laterale (VARIANTE - couleur/taille)"),
        (LOCAL_COLOR, "Relation locale (entites voisines)"),
    ]
    out = [f'<g font-family="Segoe UI, Verdana" font-size="13">']
    for i, (color, label) in enumerate(items):
        ly = y + i * 24
        out.append(f'<line x1="{x:.1f}" y1="{ly:.1f}" x2="{x+34:.1f}" y2="{ly:.1f}" stroke="{color}" stroke-width="2.4"/>')
        out.append(f'<text x="{x+44:.1f}" y="{ly+4:.1f}" fill="#3a3d5c">{html.escape(label)}</text>')
    out.append('</g>')
    return "\n".join(out)


def main():
    ents, col_x, hub_x, trunk_u_y, trunk_p_y, trunk_l_y, grid_top = build()
    rel_svg = render(ents, col_x, hub_x, trunk_u_y, trunk_p_y, trunk_l_y, grid_top)

    max_right = max(e.right for e in ents.values())
    max_bottom = max(e.bottom for e in ents.values())
    width = max_right + MARGIN
    height = max_bottom + 110  # place pour la legende + marge basse

    legend_y = max_bottom + 30

    parts = []
    parts.append(f'<?xml version="1.0" encoding="UTF-8"?>')
    parts.append(f'<svg width="{width:.0f}" height="{height:.0f}" viewBox="0 0 {width:.0f} {height:.0f}" '
                 f'xmlns="http://www.w3.org/2000/svg" font-family="Segoe UI, Verdana">')
    parts.append(f'<rect x="0" y="0" width="{width:.0f}" height="{height:.0f}" fill="{BG}"/>')

    # gouttieres (debug visuel discret : lignes pointillees tres claires)
    for ty, c in ((trunk_u_y, HUB_COLOR), (trunk_p_y, PROD_COLOR), (trunk_l_y, LATERAL_COLOR)):
        parts.append(f'<line x1="0" y1="{ty:.1f}" x2="{width:.0f}" y2="{ty:.1f}" stroke="{c}" stroke-width="0.5" stroke-dasharray="1,6" opacity="0.25"/>')

    for e in ents.values():
        parts.append(e.svg())
    parts.extend(rel_svg)

    parts.append(legend(MARGIN, legend_y))
    parts.append(f'<text x="{MARGIN:.1f}" y="{legend_y - 14:.1f}" font-size="12" fill="#8d92bd">'
                 f'23 entites - 27 associations - genere depuis mcd/zandomarketplace.mcd</text>')

    parts.append('</svg>')

    with open("zandomarketplace.svg", "w", encoding="utf-8") as f:
        f.write("\n".join(parts))

    print(f"OK: {width:.0f}x{height:.0f}")


if __name__ == "__main__":
    main()
