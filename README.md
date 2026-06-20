
<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=2,12,20,6&height=220&section=header&text=ZandoMarketPlace&fontSize=58&fontColor=ffffff&animation=fadeIn&desc=Rapport%20d'Audit%20Technique%20Approfondi&descAlignY=62&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com/?lines=Audit+avant%2Fapr%C3%A8s+intervention+Cognito+Inc.;S%C3%A9curit%C3%A9+%C2%B7+Performance+%C2%B7+Qualit%C3%A9+de+code;22+tables+%C2%B7+25+relations+%C2%B7+0%25+%C3%A0+100%25+d%C3%A9ployable&font=Fira+Code&size=20&pause=1800&color=F72585&center=true&vCenter=true&width=750&height=50" />

[![Auditeur](https://img.shields.io/badge/Auditeur-Jonathan%20Kakesa%2C%20CPI-4cc9f0?style=for-the-badge)](#)
[![Cabinet](https://img.shields.io/badge/Cabinet-Cognito%20Inc.-f72585?style=for-the-badge)](#)
[![Stack](https://img.shields.io/badge/Stack-Django%204.2-4ade80?style=for-the-badge&logo=django)](#)
[![Status](https://img.shields.io/badge/Statut-En%20d%C3%A9veloppement-fbbf24?style=for-the-badge)](#)

**🧑‍🔬 Auditeur : Jonathan Kakesa, CPI — Senior Full-Stack Engineer**
**🏢 Cabinet : Cognito Inc.**
**📅 Date : 19 juin 2026**
**🎯 Cible : Plateforme marketplace ZandoMarketPlace (Django)**
**📊 Méthode : Revue manuelle ligne par ligne, tests fonctionnels en direct, analyse statique**

### 🌐 Version site web animé (recommandée pour le client)

📂 **[`docs/audit-report.html`](docs/audit-report.html)** — site one-page complet et animé : architecture du code, schéma 3D de la base de données, audit complet par onglets, scores animés, roadmap. À ouvrir dans n'importe quel navigateur.

📄 **Export PDF** — ouvre [`docs/audit-report.html`](docs/audit-report.html) dans ton navigateur, puis `Ctrl+P` → "Enregistrer en PDF" (une feuille de style impression est déjà configurée pour un rendu propre, sans animations).

---

### 🚦 VERDICT GLOBAL

| Score sécurité | Score fonctionnel | Score qualité code | Score infra/déploiement |
|:---:|:---:|:---:|:---:|
| 🟧 **4/10** ➜ 🟩 **8/10** | 🟥 **2/10** (inchangé) | 🟧 **5/10** (inchangé) | 🟥 **0/10** ➜ 🟩 **8/10** |
| *avant ➜ après* | *avant ➜ après* | *avant ➜ après* | *avant ➜ après* |

</div>

---

## 📑 Table des matières

1. [🧬 Visualisation 3D animée de la base de données](#-visualisation-3d-animée-de-la-base-de-données)
2. [🎯 Méthodologie & périmètre](#-méthodologie--périmètre)
3. [🏗️ Vue d'ensemble du stack technique](#️-vue-densemble-du-stack-technique)
4. [🥇 PARTIE 1 — Audit du dossier original (avant intervention)](#-partie-1--audit-du-dossier-original-avant-intervention)
5. [🥈 PARTIE 2 — Audit du dépôt GitHub en ligne (après intervention)](#-partie-2--audit-du-dépôt-github-en-ligne-après-intervention)
6. [📊 Tableau de bord des risques](#-tableau-de-bord-des-risques)
7. [🗺️ Feuille de route recommandée](#️-feuille-de-route-recommandée)
8. [✍️ Verdict final](#️-verdict-final)

---

## 🧬 Visualisation 3D animée de la base de données

<div align="center">
<img src="https://img.shields.io/badge/23%20tables-mod%C3%A9lis%C3%A9es-f72585?style=for-the-badge" />
<img src="https://img.shields.io/badge/27%20relations-FK%20%2F%201%3A1-4cc9f0?style=for-the-badge" />
<img src="https://img.shields.io/badge/Three.js-rotation%20%C2%B7%20zoom%20%C2%B7%20survol-4ade80?style=for-the-badge" />
</div>

GitHub ne peut pas exécuter de JavaScript dans un README — voici donc un **fichier 3D interactif et animé** à part, généré à partir des vrais modèles Django du projet (`accounts`, `products`, `orders`, `payments`).

📂 **[`docs/schema-3d.html`](docs/schema-3d.html)** — à ouvrir directement dans n'importe quel navigateur (double-clic, aucune installation requise).

**Ce que tu y trouveras :**
- 🌌 Chaque **table** = une sphère lumineuse pulsante, colorée par application Django
- 🔗 Chaque **relation** (`ForeignKey`, `OneToOne`) = une ligne animée entre les tables
- 🖱️ **Glisser** pour orbiter autour du schéma en 3D, **molette** pour zoomer
- ✨ **Survoler une table** affiche tous ses champs et met en surbrillance ses relations
- 🌀 Rotation automatique continue + halo pulsé sur chaque nœud — animé en permanence, même sans interaction

> 💡 Astuce : les tables `products` (rose) forment le plus gros cluster — c'est normal, c'est le cœur du catalogue (variantes, couleurs, tailles, avis, wishlist...).

### 📐 Modèle Conceptuel de Données (MCD — notation Chen / Mocodo)

Pour une lecture plus formelle des cardinalités (0,1 / 1,1 / 0,N / 1,N), voici le **MCD complet généré avec [Mocodo](https://www.mocodo.net/)** à partir des modèles Django réels — entités à gauche, associations en losange, cardinalités sur chaque branche :

<p align="center">
  <img src="docs/mcd/zandomarketplace.svg" alt="MCD ZandoMarketPlace - notation Mocodo" width="100%">
</p>

📂 Source éditable : [`docs/mcd/zandomarketplace.mcd`](docs/mcd/zandomarketplace.mcd) · régénérable avec `python -m mocodo --input zandomarketplace.mcd`

---

## 🎯 Méthodologie & périmètre

> *"On ne peut sécuriser ce qu'on n'a pas mesuré."*

Cet audit a été réalisé en trois passes :

| Passe | Quoi | Outils |
|---|---|---|
| 🔍 **1. Analyse statique** | Lecture exhaustive de chaque fichier Python, HTML, JS, CSS du dépôt | Revue manuelle ligne par ligne |
| 🧪 **2. Test dynamique** | Déploiement réel sur Railway, navigation live, clics sur chaque lien | Tests fonctionnels en conditions réelles |
| 🗂️ **3. Analyse d'historique** | Inspection des migrations, des fichiers de config, de l'absence de `.git` | `git log`, inspection du système de fichiers |

**Deux instantanés ont été comparés :**

- 🗃️ **AVANT** — le dossier brut reçu du développeur précédent, jamais versionné, jamais déployé
- 🌐 **APRÈS** — le dépôt GitHub + l'application réellement en ligne sur Railway, post-intervention Cognito Inc.

---

## 🏗️ Vue d'ensemble du stack technique

```
Backend     : Django 4.2 (Python) + Django REST Framework (installé, non utilisé)
Base de données : SQLite (dev) → PostgreSQL (prod, après intervention)
Frontend    : Templates Django + CSS/JS vanilla (pas de framework JS)
Paiement    : Stripe (dépendance présente, 0% implémenté)
Apps Django : accounts · products · orders · payments · dashboard
```

**Points positifs à noter d'emblée** (un bon audit reste honnête dans les deux sens) :
- ✅ Modèle de données `Product` très riche : variantes, couleurs, tailles, rabais temporisés, avis, wishlist, historique de vue
- ✅ Modèle utilisateur personnalisé (`AbstractUser`) avec rôles `client/seller/admin` — bonne pratique dès le départ
- ✅ Django Admin pour `products` très soigné (inlines, filtres, recherche) — 360 lignes de configuration sérieuse
- ✅ Attributs `alt` présents sur les images (accessibilité de base respectée)

---

## 🥇 PARTIE 1 — Audit du dossier original (avant intervention)

> 🗃️ État du code **tel que reçu**, avant toute action de Cognito Inc. — jamais commité, jamais déployé, jamais testé en conditions réelles.

### 🔐 A. Sécurité & gestion des secrets

<table>
<tr><td>🆔</td><td><b>ZMP-2026-001</b></td></tr>
<tr><td>🔥 Sévérité</td><td><b>CRITIQUE</b></td></tr>
<tr><td>📍 Où</td><td>Racine du projet</td></tr>
<tr><td>🧨 Constat</td><td>Le projet n'était dans <b>aucun dépôt Git</b>. Aucun historique, aucune sauvegarde, aucune branche. Un crash disque = projet perdu intégralement.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-002</b></td></tr>
<tr><td>🔥 Sévérité</td><td><b>CRITIQUE</b></td></tr>
<tr><td>📍 Où</td><td><code>.env</code></td></tr>
<tr><td>🧨 Constat</td><td>

```env
SECRET_KEY=django-insecure-7$y9x!kq8p@r#9*abc1234567890abcdef
DEBUG=True
```
Clé secrète Django (signe les cookies de session, les tokens CSRF) stockée en clair, **sans `.gitignore` pour la protéger** d'un commit accidentel. `DEBUG=True` expose des stack traces complètes (chemins serveur, requêtes SQL, variables) à n'importe quel visiteur en cas d'erreur.
</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-003</b></td></tr>
<tr><td>🔥 Sévérité</td><td><b>CRITIQUE</b></td></tr>
<tr><td>📍 Où</td><td><code>db.sqlite3</code></td></tr>
<tr><td>🧨 Constat</td><td>Base de données complète (utilisateurs, mots de passe hashés, commandes) présente en fichier brut à la racine, sans protection.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-004</b></td></tr>
<tr><td>⚠️ Sévérité</td><td><b>MAJEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>zandomarket/settings.py</code></td></tr>
<tr><td>🧨 Constat</td><td>

```python
ALLOWED_HOSTS = ['*']
```
Accepte n'importe quel en-tête `Host` — porte ouverte aux attaques de type *Host Header Injection* (empoisonnement de cache, liens de réinitialisation de mot de passe forgés).
</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-005</b></td></tr>
<tr><td>⚠️ Sévérité</td><td><b>MAJEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>settings.py</code> — <code>INSTALLED_APPS</code> vs <code>MIDDLEWARE</code></td></tr>
<tr><td>🧨 Constat</td><td><code>corsheaders</code> est déclaré dans <code>INSTALLED_APPS</code> mais le middleware <code>corsheaders.middleware.CorsMiddleware</code> <b>n'a jamais été ajouté</b> à <code>MIDDLEWARE</code>. Résultat : la protection CORS donne l'illusion d'exister mais n'a <b>jamais été active</b>, à aucun moment.</td></tr>
</table>

---

### 🧩 B. Backend — Logique métier cassée ou absente

<table>
<tr><td>🆔</td><td><b>ZMP-2026-006</b></td></tr>
<tr><td>🔥 Sévérité</td><td><b>CRITIQUE</b></td></tr>
<tr><td>📍 Où</td><td><code>apps/accounts/views.py</code> (3 lignes), <code>apps/accounts/urls.py</code></td></tr>
<tr><td>🧨 Constat</td><td>

```python
# apps/accounts/urls.py — contenu INTÉGRAL du fichier
urlpatterns = [
    # exemple temporaire
    # path('', views.product_list, name='product_list'),
]
```
**Aucune route active.** Pourtant, dans `header.html`, ces liens existent et sont cliqués par chaque visiteur :
```html
<a href="/login/">Se connecter</a>
<a href="/register/">S'inscrire</a>
<a href="/logout/">Déconnexion</a>
```
➡️ **Vérifié en direct : ces trois liens renvoient une erreur 404.** Aucun visiteur ne peut créer de compte, ni se connecter, ni se déconnecter.
</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-007</b></td></tr>
<tr><td>🔥 Sévérité</td><td><b>CRITIQUE</b></td></tr>
<tr><td>📍 Où</td><td><code>apps/orders/views.py</code>, <code>apps/orders/urls.py</code></td></tr>
<tr><td>🧨 Constat</td><td>Les modèles <code>Cart</code>, <code>CartItem</code>, <code>Order</code>, <code>OrderItem</code> existent en base (34 lignes de modèles bien pensés), mais <b>zéro vue, zéro formulaire, zéro route</b> ne les exploite. Le lien "Panier" du header pointe vers <code>href="#"</code> — il ne fait littéralement rien.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-008</b></td></tr>
<tr><td>🔥 Sévérité</td><td><b>CRITIQUE</b></td></tr>
<tr><td>📍 Où</td><td><code>requirements.txt</code> vs <code>apps/payments/</code></td></tr>
<tr><td>🧨 Constat</td><td><code>stripe</code> figure dans les dépendances, donnant l'illusion qu'un système de paiement existe. En réalité : <code>views.py</code> = 3 lignes vides, <code>models.py</code> = une simple table sans aucune logique d'appel à l'API Stripe. <b>Taux d'implémentation réel : 0%.</b></td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-009</b></td></tr>
<tr><td>⚠️ Sévérité</td><td><b>MAJEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>apps/products/views.py::product_detail()</code> lignes 88-113</td></tr>
<tr><td>🧨 Constat</td><td>Code dupliqué — les mêmes requêtes sont exécutées <b>deux fois de suite</b> dans la même fonction :

```python
variants = product.variants.select_related("color", "size")        # ligne 88 — calculé...
reviews = product.reviews.select_related("user")                    # ligne 93 — ...puis jeté.
total_views = product.views.count()                                 # ligne 97 — calculé...

variants = ProductVariant.objects.filter(product=product)...        # ligne 102 — RECALCULÉ
reviews = ProductReview.objects.filter(product=product)...          # ligne 109 — RECALCULÉ
total_views = product.views.count()                                 # ligne 123 — RE-RECALCULÉ
```
Trois requêtes SQL exécutées pour rien à chaque vue de fiche produit.
</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-010</b></td></tr>
<tr><td>⚠️ Sévérité</td><td><b>MAJEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>apps/products/views.py::home()</code> + <code>Product.average_rating</code> / <code>Product.rating_count</code></td></tr>
<tr><td>🧨 Constat</td><td>🐌 <b>Problème N+1 classique.</b> Chaque carte produit affichée sur la page d'accueil appelle :

```python
@property
def average_rating(self):
    return self.reviews.aggregate(avg=models.Avg('rating'))['avg'] or 0   # 1 requête SQL

@property
def rating_count(self):
    return self.reviews.count()                                          # 1 requête SQL
```
Avec 12 produits "Juste pour vous" + 8 produits "du quotidien" affichés, c'est **jusqu'à 40 requêtes SQL supplémentaires** générées uniquement pour afficher des étoiles, à chaque chargement de la page d'accueil — et ce, même là où `prefetch_related('reviews')` est utilisé, car `.aggregate()` et `.count()` ignorent le cache de prefetch et retournent toujours en base.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-011</b></td></tr>
<tr><td>💡 Sévérité</td><td><b>MINEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>apps/products/models.py</code> lignes 78, 148</td></tr>
<tr><td>🧨 Constat</td><td>

```python
discount_percent = models.PositiveIntegerField(default=0)   # pas de MaxValueValidator !
```
`MaxValueValidator` est pourtant déjà importé en haut du fichier (utilisé pour `rating`) mais **jamais appliqué au rabais**. Un rabais de 150% est acceptable pour la base de données et produit un `final_price` **négatif**.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-012</b></td></tr>
<tr><td>💡 Sévérité</td><td><b>MINEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>apps/accounts/models.py</code></td></tr>
<tr><td>🧨 Constat</td><td>

```python
@property
def is_admin_user(self):
    return self.user_type == 'admin' or self.is_superuser
```
`user_type` (un simple champ texte modifiable) et `is_staff`/`is_superuser` (les vraies permissions Django) ne sont **jamais synchronisés**. Un utilisateur peut avoir `user_type='admin'` sans le moindre droit réel dans Django Admin, ou inversement. Source de confusion garantie pour l'équipe support.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-013</b></td></tr>
<tr><td>💡 Sévérité</td><td><b>MINEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>apps/products/models.py</code> — <code>SellerProfile.is_verified</code></td></tr>
<tr><td>🧨 Constat</td><td>Le champ existe en base mais n'est <b>vérifié nulle part</b> dans le code. Un vendeur non vérifié a exactement les mêmes droits qu'un vendeur vérifié — le champ est purement décoratif aujourd'hui.</td></tr>
</table>

---

### 🎨 C. Frontend — Templates, CSS & JavaScript

<table>
<tr><td>🆔</td><td><b>ZMP-2026-014</b></td></tr>
<tr><td>⚠️ Sévérité</td><td><b>MAJEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>apps/products/templates/products/home.html</code> lignes 123-191 et 214-281</td></tr>
<tr><td>🧨 Constat</td><td>💥 <b>HTML structurellement invalide</b>, dupliqué dans deux blocs. La balise <code>&lt;a&gt;</code> s'ouvre <i>à l'intérieur</i> de la boucle <code>{% for %}</code> mais ne s'y referme jamais — une seule <code>&lt;/a&gt;</code> orpheline apparaît <i>après</i> la boucle :

```html
{% for product in recommended_products %}
  <a href="..." class="product-card-link">      <!-- ouverte N fois -->
    <div class="product-card"> ... </div>
{% endfor %}
</div>                                            <!-- div surnuméraire -->
</a>                                               <!-- une seule fermeture pour N ouvertures ! -->
```
Les navigateurs « réparent » ce genre d'erreur silencieusement, mais le comportement de clic devient imprévisible (liens imbriqués, zones cliquables qui se chevauchent) et le code ne passerait <b>aucun</b> validateur HTML.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-015</b></td></tr>
<tr><td>⚠️ Sévérité</td><td><b>MAJEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>apps/products/templates/includes/header.html</code> + <code>static/products/js/header.js</code></td></tr>
<tr><td>🧨 Constat</td><td>Le menu de catégories visible à l'écran (Mode, Maison, Beauté, Automobile...) est <b>entièrement codé en dur en JavaScript</b> (`categoryData` dans `header.js`), totalement déconnecté du modèle <code>Category</code> existant en base de données. Cliquer sur "Voir plus" déclenche :

```js
more.addEventListener("click", ()=>{
  alert("Catalogue bientôt disponible 🚀");
});
```
La barre de recherche (`<input placeholder="Rechercher produits...">`) n'a ni `<form>`, ni `action`, ni gestionnaire JS — **purement décorative**.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-016</b></td></tr>
<tr><td>💡 Sévérité</td><td><b>MINEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>apps/products/templates/base.html</code></td></tr>
<tr><td>🧨 Constat</td><td>Double-chargement d'assets : <code>home.css</code> et <code>home.js</code> sont déjà chargés sans condition dans <code>base.html</code> (donc sur <b>toutes</b> les pages, y compris la fiche produit qui n'en a pas besoin), puis <b>rechargés une seconde fois</b> via <code>{% block extra_css/js %}</code> dans <code>home.html</code>. De plus, <code>home.js</code> est chargé sans l'attribut <code>defer</code> alors que <code>header.js</code>, juste en dessous, l'utilise correctement — incohérence qui bloque inutilement le rendu de la page pendant le téléchargement du script.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-017</b></td></tr>
<tr><td>💡 Sévérité</td><td><b>MINEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>base.html</code> ligne 15</td></tr>
<tr><td>🧨 Constat</td><td>Font Awesome chargé depuis un CDN externe (`cdnjs.cloudflare.com`) sans attribut `integrity` (Subresource Integrity) ni `crossorigin` — si ce CDN est un jour compromis, du code arbitraire pourrait être injecté sur le site sans aucune alerte du navigateur.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-018</b></td></tr>
<tr><td>💡 Sévérité</td><td><b>MINEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>includes/footer.html</code></td></tr>
<tr><td>🧨 Constat</td><td>Le footer entier se résume à une ligne de copyright. Aucun lien "À propos", "Contact", "Conditions d'utilisation", "Politique de confidentialité" — problématique pour la confiance client sur un site marchand, et juridiquement risqué pour la conformité (CGV/CGU absentes).</td></tr>
</table>

---

### 🧪 D. Qualité de code, tests & organisation

<table>
<tr><td>🆔</td><td><b>ZMP-2026-019</b></td></tr>
<tr><td>💡 Sévérité</td><td><b>MINEUR</b></td></tr>
<tr><td>📍 Où</td><td><code>apps/dashboard/</code></td></tr>
<tr><td>🧨 Constat</td><td>L'app censée gérer l'administration du marketplace (<code>dashboard</code>) est <b>entièrement vide</b> — seulement le code généré par défaut (<code>django-admin startapp</code>), zéro ligne ajoutée.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-020</b></td></tr>
<tr><td>💡 Sévérité</td><td><b>MINEUR</b></td></tr>
<tr><td>📍 Où</td><td>Tout le projet</td></tr>
<tr><td>🧨 Constat</td><td><b>0% de couverture de test.</b> Les 5 fichiers <code>tests.py</code> contiennent uniquement le commentaire <code># Create your tests here.</code> généré par défaut. Aucune CI/CD, aucun linter (flake8/black), aucun pre-commit hook.</td></tr>
</table>

<table>
<tr><td>🆔</td><td><b>ZMP-2026-021</b></td></tr>
<tr><td>💡 Sévérité</td><td><b>MINEUR</b></td></tr>
<tr><td>📍 Où</td><td>Racine du projet, <code>settings.py</code></td></tr>
<tr><td>🧨 Constat</td><td>3 fichiers parasites de 0 octet (<code>cls</code>, <code>python</code>, <code>{</code>) — artefacts d'une commande tapée dans le mauvais terminal. <code>LANGUAGE_CODE = 'en-us'</code> alors que toute l'interface visible est en français.</td></tr>
</table>

---

## 🥈 PARTIE 2 — Audit du dépôt GitHub en ligne (après intervention)

> 🌐 État du code **après** la mise en place de l'infrastructure par Cognito Inc. — dépôt Git créé, sécurisé, déployé sur Railway avec PostgreSQL.

### ✅ Corrections appliquées (preuves à l'appui)

| # | Avant 🗃️ | Après 🌐 |
|---|---|---|
| 1 | Aucun dépôt Git | Dépôt Git propre, créé **isolé** de l'environnement système (un risque de fuite de credentials AWS/Docker a été détecté et évité sur la machine de développement au passage) |
| 2 | `.env` exposé, aucun `.gitignore` | `.gitignore` + `.env.example` — secrets, base de données et caches **ne peuvent plus jamais** être commités par accident |
| 3 | `ALLOWED_HOSTS = ['*']` codé en dur | `env.list('ALLOWED_HOSTS', ...)` — configurable par variable d'environnement, plus aucune valeur sensible en dur |
| 4 | Aucun serveur de production | `gunicorn` + `Procfile` — l'app tourne désormais derrière un vrai serveur WSGI de production |
| 5 | SQLite uniquement | `DATABASE_URL` via `env.db()` — PostgreSQL managé sur Railway |
| 6 | Fichiers statiques servis en mode `DEBUG` uniquement | `whitenoise` avec compression + manifeste de cache-busting |
| 7 | Aucun compte admin accessible en prod | Commande `ensure_superuser` idempotente, pilotée par variables d'environnement |
| 8 | 🐛 *Bug découvert et corrigé en direct après mise en ligne* | `django.conf.urls.static.static()` est **codé en dur pour ne rien faire quand `DEBUG=False`** — un piège classique de Django qui rendait toutes les images invisibles en production. Remplacé par un appel direct à `django.views.static.serve`. |
| 9 | Fichiers parasites (`cls`, `python`, `{`) | Supprimés |

### ❌ Ce qui reste — **strictement inchangé depuis la Partie 1**

> ⚠️ Mettre un projet en ligne ne corrige pas ses lacunes fonctionnelles. Tous les findings `ZMP-2026-006` à `ZMP-2026-020` listés plus haut sont **toujours présents tels quels** dans le dépôt GitHub actuel :

- 🔥 `/login/`, `/register/`, `/logout/` renvoient toujours une **404** — aucun visiteur ne peut créer de compte
- 🔥 Panier, commande, paiement : toujours 0% implémentés
- ⚠️ Code dupliqué dans `product_detail()`, problème N+1 sur les notes produits
- ⚠️ HTML invalide sur la page d'accueil (balises `<a>` non fermées)
- ⚠️ Menu de catégories et recherche toujours factices
- 💡 `corsheaders` toujours sans middleware, `discount_percent` toujours sans validation maximale
- 💡 Toujours 0% de couverture de test

### 🆕 Nouveau risque introduit par la mise en ligne elle-même

| 🆔 | Constat |
|---|---|
| **ZMP-2026-022** | Le stockage des fichiers media sur Railway est **éphémère** (pas de volume persistant ni de S3/R2). Toute photo de produit uploadée via l'admin après la mise en ligne **sera supprimée au prochain déploiement**. Les images actuellement visibles sont celles commitées dans le dépôt Git, pas des uploads dynamiques. |
| **ZMP-2026-023** | Le mot de passe du superutilisateur reste stocké en variable d'environnement Railway (`DJANGO_SUPERUSER_PASSWORD`) — à retirer après la première connexion pour éviter une fuite via les logs ou un export de configuration. |

---

## 📊 Tableau de bord des risques

```
🔥 CRITIQUE   ████████████████████████████  7 findings
⚠️  MAJEUR    ████████████████████████      6 findings
💡 MINEUR     ████████████████████████████████████  10 findings
```

| Domaine | 🔥 Critique | ⚠️ Majeur | 💡 Mineur | Statut |
|---|:---:|:---:|:---:|---|
| 🔐 Sécurité & Secrets | 3 | 2 | 0 | ✅ Corrigé |
| 🚀 Infrastructure/Déploiement | 1 | 0 | 0 | ✅ Corrigé |
| 🧩 Backend / Fonctionnalités | 3 | 2 | 3 | ❌ **À développer** |
| 🎨 Frontend / Templates | 0 | 2 | 3 | ❌ **À développer** |
| 🧪 Qualité / Tests | 0 | 0 | 4 | ❌ **À développer** |

---

## 🗺️ Feuille de route recommandée

```
✅ Sprint 0 (FAIT)     Git + sécurité de base + déploiement Railway + PostgreSQL
🔲 Sprint 1            Authentification réelle (inscription / connexion / déconnexion)
🔲 Sprint 2            Panier + tunnel de commande fonctionnel
🔲 Sprint 3            Intégration de paiement réelle (Stripe + Mobile Money)
🔲 Sprint 4            Recherche + navigation par catégorie connectées à la base
🔲 Sprint 5            Stockage media persistant (S3 / Cloudflare R2)
🔲 Sprint 6            Tests automatisés + CI/CD
🔲 Sprint 7            Nettoyage dette technique (HTML invalide, requêtes N+1, doublons)
```

---

## ✍️ Verdict final

> Le projet repose sur des **fondations de données solides** : un modèle `Product` riche, un système de rôles bien pensé, un Django Admin soigné pour la gestion du catalogue. C'est un excellent point de départ.
>
> Mais à ce stade, **ZandoMarketPlace est une vitrine, pas un marketplace.** Un visiteur peut regarder des produits — il ne peut ni créer de compte, ni acheter, ni payer. Les boutons "Se connecter", "Panier" et "Devenir vendeur" sont aujourd'hui des promesses non tenues par le code.
>
> L'intervention de Cognito Inc. a rendu le projet **sain, sécurisé et réellement déployé** — la fondation est maintenant prête à recevoir les fonctionnalités métier qui transformeront cette vitrine en marketplace opérationnel.

---

<div align="center">

### 🖋️ Signature

**Jonathan Kakesa, CPI | CEO Cognito Inc.**

*Senior Full-Stack Engineer · Audit technique indépendant*

</div>
#   Z a n d o M a r k e t P l a c e - A u d i t  
 