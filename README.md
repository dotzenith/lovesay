<h2 align="center"> ━━━━━━  ❖  ━━━━━━ </h2>

<!-- BADGES -->
<div align="center">
   <p></p>
   
   <img src="https://img.shields.io/github/stars/zenithds/lovesay?color=F8BD96&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/forks/zenithds/lovesay?color=DDB6F2&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/repo-size/zenithds/lovesay?color=ABE9B3&labelColor=302D41&style=for-the-badge">
   
   <img src="https://badges.pufler.dev/visits/zenithds/lovesay?style=for-the-badge&color=96CDFB&logoColor=white&labelColor=302D41"/>
   <br>
</div>

<p/>

---

### ❖ Information 

  lovesay is a simple and lightweight python script that displays a quote from a loved one based on the day of the month 

  <img src="assets/lovesay.gif" alt="lovesay gif">

---

### ❖ Requirements 

- A quotes file stored in `$HOME/.config/lovesay/`
- Each quote must be on a new line, see the example quotes file in `$HOME/.config/lovesay/quotes`
- (optional) A partner to write you 31 lines full of love, one for each day of the month

---

### ❖ Installation

> Install from pip
```sh
$ pip3 install lovesay
```

> Install from source
- First, install [poetry](https://python-poetry.org/)
```sh
$ git clone https://github.com/ZenithDS/lovesay.git
$ cd lovesay
$ poetry install
```

### ❖ Usage 

lovesay can be used with a variety of different color schemes.

> lovesay uses [catppuccin](https://github.com/catppuccin) as it's default color scheme, but a different one can be specified using a positional argument. 

For example:
```sh
$ lovesay # uses catppuccin
```
  
```sh
$ lovesay nord # uses nord 
```

Supported color schemes as of now: 
> [catppuccin](https://github.com/catppuccin)
> [nord](https://github.com/arcticicestudio/nord)
> [dracula](https://github.com/dracula/dracula-theme)
> [gruvbox](https://github.com/morhetz/gruvbox)
> [onedark](https://github.com/joshdick/onedark.vim)

by default, lovesay checks for the quotes file at `$HOME/.config/lovesay/quotes` if there is nothing there, it will just print out a heart with no quote

---

### ❖ About lovesay

I wrote lovesay because I got tired of seeing neofetch or pfetch every time I opened my terminal. I wanted something more personal. 

Seeing words full of love from my partner is a lot better than any other command I could possibly run. It makes my terminal feel cozy, welcoming, and as is the case with most things my partner touches, it makes my terminal feel like home. 

I hope that someone else finds a use for this little script as well. Love is a wonderful thing, and we could all use a little bit more of it in our lives (especially arch linux users)

---

### ❖ What's New? 
0.2.1 - lovesay now has themes :)

---

<div align="center">

   <img src="https://img.shields.io/static/v1.svg?label=License&message=MIT&color=F5E0DC&labelColor=302D41&style=for-the-badge">

</div>
