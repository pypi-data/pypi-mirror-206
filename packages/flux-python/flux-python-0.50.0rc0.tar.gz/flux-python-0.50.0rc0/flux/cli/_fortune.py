##############################################################
# Copyright 2023 Lawrence Livermore National Security, LLC
# (c.f. AUTHORS, NOTICE.LLNS, COPYING)
#
# This file is part of the Flux resource manager framework.
# For details, see https://github.com/flux-framework.
#
# SPDX-License-Identifier: LGPL-3.0
##############################################################

import argparse
import random
import sys

import flux.util
from flux.cli import base

# Choice of decorating symbols
symbols = ["@", "*", "**", "!", "$", "%", "^", "O", "o", "|", "x", "8", "*", "{*}", "-"]

# Choices of colors to print
colors = [
    "\033[91m %s %s %s\033[00m",  # red
    "\033[92m %s %s %s\033[00m",  # green
    "\033[93m %s %s %s\033[00m",  # yellow
    "\033[95m %s %s %s\033[00m",  # magenta
    "\033[94m %s %s %s\033[00m",  # blue
    "\033[96m %s %s %s\033[00m",  # cyan
    "\033[97m %s %s %s\033[00m",
]  # gray


class FortuneCmd(base.MiniCmd):
    """
    Surprise the user with some beautiful, hidden Flux fortunes and art!

    Usage: flux fortune
    """

    @staticmethod
    def create_parser(
        prog, usage=None, description=None, exclude_io=False, add_help=True
    ):
        """
        Create a largely empty parser for flux fortune (no arguments or exposed)
        """
        if usage is None:
            usage = f"{prog} [OPTIONS...] COMMAND [ARGS...]"
        return argparse.ArgumentParser(
            prog=prog,
            usage=usage,
            description=description,
            formatter_class=flux.util.help_formatter(),
        )

    def generate_fortune(self):
        """
        Generate the fortune, meaning:

        1. Choose to print a fortune (a) or the (rare) ascii art.
        2. If a, choose a color and print.
        3. If b, print the ascii and exit.
        """
        # 1% chance to print ascii art
        if random.uniform(0, 1) <= 0.01:
            print(random.choice(art))
            return

        # Otherwise, choose a color and a fortune...
        color = random.choice(colors)
        s = random.choice(symbols)
        fortune = random.choice(fortunes)
        print(color % (s, fortune, s))

    def main(self, args):
        self.generate_fortune()
        sys.exit(self.exitcode)


# Fortunes (a filtered set) from https://github.com/vsoch/boxes
fortunes = [
    "I refuse to have modem speeds without the sweet modem sounds",
    "Man who run in front of car get tired.",
    "Sneeze on ice cube tray, have very strange problem.",
    "Man who eat many prunes get good run for money.",
    "Baseball is wrong - man with four balls cannot walk.",
    "If you want to see mankind's real fog of war, take a look at the dark side of Pluto on Google Maps with webGL.",
    "It take many nails to build crib but one screw to fill it.",
    "Man who drive like hell bound to get there.",
    "He who sitteth on an upturned tack shall surely rise.",
    "A yawn is a silent scream for coffee.",
    "Even the greatest of whales is helpless in middle of desert.",
    "I don't trust that horse... he's a naysayer!",
    "Man who sit on tack get point!",
    "I have phantom fart syndrome. I smell farts when there aren't any.",
    "In grade school they told me to enunciate my words. But I don’t. I string them together. I talk in cursive.",
    "What kind of 'eenie lives in a zoo? The zucchini, of course.",
    "Due to a shortage of robots, our staff is composed of humans and may react unpredictably when abused.",
    "Man who jumps off cliff, jumps to concussion!",
    "Dear <software>, stop doing <that>. Thank you. Best, <developer>",
    "Dear Flux, I don't need your bad jokes. Thanks. Best, <flux-user>",
    "The best kind of HPC system I can imagine would smell like cookies. Forever.",
    "Quiet in a Slack doesn’t mean that people aren’t talking, it means that they just aren’t talking to you.",
    "In 1970 they blew up a whale carcass in Oregon with 1/2 ton of dynamite.",
    "If someone asks me where I am in my life right now, I’d say the other day I ran through a snow storm to get free breakfast. And no one was there.",
    "Tensorflow? Or more like TensorNO.",
    "Help me, I'm trapped in a container!",
    "The multiplication of smells to produce a combined whole: Integration by farts.",
    "If you fart and burp at the same time, you take a screenshot.",
    "Did you catch a piece of cauliflower on fire in the microwave, or are you really an adult?",
    "Who would win, 100 duck sized cows, or 1 cow sized duck?",
    "Real roads have curbs.",
    "I went to visit Shaq O’Neill on his animal farm. He has boom shakalamas!",
    "Ladies and gentleman, 'tacos cat'!",
    "You don’t need to worry about getting older when you’re a robot… it’s just a one digit progression in your time-stamp.",
    "The opposite of 'Feel the Bern' could be 'Feel the Breeze,' so under this logic I conclude that if I ran into a group of Anti Bernie Sanders folks, their self-identifying feature would be not wearing any pants.",
    "When repeating a word and it sounds weird and unfamiliar, that has a name, 'Semantic Satiation.'",
    "Man who stick foot in mouth get athlete's tongue!",
    "Man who live in glass house should not throw parties!",
    "When called an idiot sometimes is better to be quiet, than open mouth and remove all doubt.",
    "Man with glass house must dress in basement!",
    "Everyone has a photographic memory, some people just don't have film!",
    "Sweet dreams are made of cheese... who am I to diss a brie?",
    "He who stands on toilet, is high on throne.",
    "I thought America was already great, but what really sealed the deal was the KFC Fried Chicken Scented Candle.",
    "He who eats too many prunes, sits on toilet many moons.",
    "Work to become, not to acquire.",
    "I reached for my mouse... grabbed an avocado instead.",
    "Mindlessly munching your asparagus? Find a piece that's especially chewy? Oh, that's because it's a rubber-band.",
    "A bird in hand makes hard to blow nose.",
    "Man who put head on Railroad track to listen for train likely to end up with splitting headache.",
    "Man who tell one too many light bulb jokes will soon burn out!",
    "One could predict light bulb age based on bug accumulation in the fixture.",
    "War does not determine who's right, war determines who's left.",
    "Man who behaves like an ass will be the butt of those who crack jokes.",
    "Man who run behind car get exhausted.",
    "Man with one chopstick go hungry.",
    "The inevitable outcome of spontaneously generating drain flies is that everything will be covered in Windex.",
    "A bug in the hair is one less in the mouth. And as luck would have it, most bugs that wind up in the mouth have hair.",
    "When you find one sock but not the other, hopefully they can put aside their differences and be friends.",
    "Found pair of underwear in pant leg. It's been there all day.",
    "He who thinks only of number one is next to nothing.",
    "Man who farts in church sits in his own pew!",
]

# This can be appended with new art as desired
art = [
    """
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m.[0m[37m'[0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m  [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m [0m[37m [0m[36mo[0m[37m,[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[34m.[0m[34m.[0m[34m.[0m[34m.[0m[34m.[0m[34m.[0m[34m.[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[36mk[0m[37m.[0m[37m.[0m[34m.[0m[34m'[0m[34m,[0m[34m'[0m[34m.[0m[34m.[0m[37m.[0m[34m.[0m[34m,[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m [0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[36ml[0m[34ml[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[34m,[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m   [37m [0m[37m.[0m[37m,[0m[36m:[0m[37m:[0m[37m:[0m[37m;[0m[37m,[0m[37m'[0m[37m'[0m[37m'[0m[37m,[0m[37m,[0m[37m:[0m[36m:[0m[36m:[0m[37m;[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m [0m[37m [0m[37m [0m[37m'[0m[34m;[0m[34m'[0m[34m'[0m[34m,[0m[34m'[0m[37m [0m[37m [0m[37m [0m [37m [0m[37m [0m[37m [0m[37m.[0m[34m.[0m[34m'[0m[34m'[0m[34m'[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m  [37m [0m[37m.[0m[37m:[0m[36mo[0m[36m:[0m[37m.[0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m [0m[37m [0m[37m.[0m[37m:[0m[36mo[0m[37m;[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[34m.[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m  [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m [0m[37m,[0m[36mo[0m[37m,[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m,[0m[36m:[0m[36mc[0m[36mc[0m[36m:[0m[37m:[0m[37m;[0m[37m;[0m[36m:[0m[36m:[0m[36mc[0m[36m:[0m[37m'[0m[37m.[0m[37m,[0m[36mo[0m[37m,[0m[37m [0m [37m [0m[34m.[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m  [37m [0m[37m.[0m[36ml[0m[36ml[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[36ml[0m[36ml[0m[37m'[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m;[0m[36mo[0m[36m:[0m[37m.[0m[36mo[0m[36mc[0m[37m [0m[34m.[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[34m.[0m[37m [0m[37m [0m[37m.[0m[37m,[0m[37m:[0m[36m:[0m[36m:[0m[37m:[0m[37m:[0m[36m:[0m[36m:[0m[36mc[0m[36m:[0m[37m,[0m[37m.[0m[37m [0m[37m [0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[36md[0m[37m,[0m[37m [0m[37m [0m[37m [0m[37m.[0m[36ml[0m[36m:[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m'[0m[37m:[0m[37m:[0m[37m:[0m[37m:[0m[36m:[0m[36m:[0m[36m:[0m[36mc[0m[37m;[0m[37m.[0m[37m,[0m[36mo[0m[36mc[0m[36mo[0m[34m:[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[36m;[0m[36mc[0m[36mc[0m[37m;[0m[37m,[0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m.[0m[37m;[0m[36mc[0m[36mc[0m[37m'[0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m'[0m[36mx[0m[37m'[0m[37m [0m[37m [0m[37m [0m[37m;[0m[36md[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m.[0m[36mc[0m[36ml[0m[37m,[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m,[0m[34ml[0m[34mc[0m[36m;[0m[34ml[0m[34mc[0m[34m,[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[34m;[0m[34m'[0m[34m'[0m[34m,[0m[34m;[0m[34m,[0m[34m,[0m[34m;[0m[37m;[0m[36m:[0m[36mc[0m[36mc[0m[36m:[0m[37m'[0m[37m [0m[37m [0m[37m [0m[37m.[0m[36m:[0m[36mo[0m[37m,[0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m [37m.[0m[36md[0m[37m'[0m[37m [0m  [37m,[0m[36md[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m,[0m[36md[0m[37m'[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[34m,[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[34m,[0m[34m,[0m[34m:[0m[34mc[0m[34mc[0m[34mc[0m[34mc[0m[34mc[0m[34m;[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m;[0m[36ml[0m[37m:[0m[37m [0m [37m [0m[37m.[0m[36mc[0m[36mo[0m[37m.[0m[37m [0m[37m [0m
[37m [0m[37m [0m[36mo[0m[36m:[0m[37m [0m[37m [0m [37m [0m[36mo[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m;[0m[36md[0m[37m.[0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[34m;[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m:[0m[36ml[0m[36mc[0m[37m;[0m[37m'[0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m;[0m[36mc[0m[36ml[0m[37m,[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m,[0m[36mo[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m,[0m[36md[0m[37m.[0m[37m [0m
[37m [0m[36mc[0m[36mO[0m[37m.[0m[37m [0m[37m [0m[37m [0m[36m:[0m[36m:[0m[37m [0m[37m [0m[37m [0m[37m'[0m[36mk[0m[37m.[0m[37m [0m[37m [0m  [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m   [37m [0m[37m [0m[37m [0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[34mc[0m[37m.[0m[37m [0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m;[0m[36mo[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m.[0m[36md[0m[37m'[0m[37m [0m[37m [0m[37m [0m[37m;[0m[36md[0m[37m [0m
[37m;[0m[36mk[0m[36mk[0m[36m:[0m[37m [0m[37m [0m[36mc[0m[36mO[0m[37m;[0m[37m [0m[37m [0m[37m.[0m[36mx[0m[36ml[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m [0m[34m.[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m;[0m[37m.[0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m.[0m[36mo[0m[37m:[0m[37m [0m[37m [0m [37m.[0m[36md[0m[37m.[0m[37m [0m [37m [0m[36md[0m[37m;[0m
[37m [0m[36mo[0m[36m:[0m[37m [0m[37m [0m[37m.[0m[36ml[0m[36mk[0m[36m:[0m[37m [0m[37m.[0m[36mx[0m[36mO[0m[36mx[0m[37m.[0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[37m.[0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[36mk[0m[37m.[0m[37m [0m[37m [0m[37m [0m[36mc[0m[36mc[0m[37m [0m[37m [0m[37m [0m[37m;[0m[36md[0m
[37m [0m[36md[0m[36m:[0m[37m [0m  [37m;[0m[36md[0m[37m [0m[37m [0m[37m [0m[37m:[0m[36mk[0m[37m,[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[37m [0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[36mo[0m[37m:[0m[37m [0m[37m [0m[37m [0m[36m:[0m[36ml[0m[37m [0m[37m [0m[37m [0m[37m'[0m[36mx[0m
 [36mo[0m[36mc[0m[37m [0m[37m [0m [37m,[0m[36mx[0m[37m [0m [37m [0m[37m'[0m[36mk[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[37m.[0m   [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [36ml[0m[37m:[0m[37m [0m[37m [0m[37m [0m[36m:[0m[36mc[0m[37m [0m[37m [0m[37m [0m[37m.[0m[36mx[0m
[37m [0m[36m:[0m[36md[0m[37m [0m[37m [0m[37m [0m[37m.[0m[36mk[0m[37m.[0m[37m [0m[37m [0m[37m [0m[36mo[0m[36m:[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m  [37m [0m[37m.[0m[34m,[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[36mx[0m[37m'[0m[37m [0m[37m [0m[37m [0m[36mo[0m[36m:[0m[37m [0m[37m [0m[37m [0m[37m,[0m[36mo[0m
[37m [0m[37m.[0m[36mk[0m[37m;[0m[37m [0m[37m [0m[37m [0m[37m;[0m[36ml[0m[37m [0m[37m [0m[37m [0m[37m.[0m[36md[0m[36m:[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[36mo[0m[36mk[0m[37m.[0m[37m [0m[37m [0m[37m,[0m[36mO[0m[37m,[0m[37m [0m [37m [0m[36mo[0m[37m;[0m
[37m [0m[37m [0m[37m;[0m[36mk[0m[37m.[0m[37m [0m[37m [0m[37m [0m[36mc[0m[36m:[0m[37m [0m [37m [0m[37m [0m[36mc[0m[36mo[0m[37m'[0m[37m [0m[37m [0m[37m [0m[37m [0m  [37m [0m[37m [0m[37m.[0m[37m;[0m[34ml[0m[34m,[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m:[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m.[0m[36mx[0m[36mO[0m[36mk[0m[37m.[0m[37m [0m[37m;[0m[36mk[0m[36mO[0m[37m'[0m[37m [0m[37m [0m[37m'[0m[36mk[0m[37m'[0m
[37m [0m[37m [0m[37m [0m[36m:[0m[36mx[0m[37m'[0m[37m [0m[37m [0m[37m [0m[36m:[0m[36mo[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m;[0m[36mc[0m[36mc[0m[36m:[0m[37m;[0m[37m;[0m[37m;[0m[36m:[0m[36mc[0m[36ml[0m[36md[0m[34m;[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34mo[0m[37m:[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m,[0m[36mk[0m[37m:[0m[37m.[0m[37m [0m[37m [0m[36mc[0m[36mx[0m[36mo[0m[37m,[0m[37m [0m[36mc[0m[36mk[0m[36mO[0m[37m;[0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m,[0m[36mx[0m[36m:[0m[37m [0m[37m [0m[37m [0m[37m.[0m[36mc[0m[36ml[0m[37m;[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m.[0m[37m.[0m[37m,[0m[36m:[0m[36mo[0m[34ml[0m[34m,[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m:[0m[36mc[0m[36md[0m[36m:[0m[37m [0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[36mc[0m[36mx[0m[37m,[0m[37m [0m [37m [0m[37m.[0m[36mo[0m[37m.[0m[37m [0m [37m [0m[37m;[0m[36mk[0m[37m;[0m[37m.[0m
[37m [0m[37m [0m[37m [0m [37m [0m[37m [0m[37m;[0m[36ml[0m[37m;[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m,[0m[37m:[0m[37m:[0m[37m:[0m[37m:[0m[37m:[0m[37m:[0m[37m:[0m[37m:[0m[37m;[0m[36m:[0m[36mc[0m[34m;[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m:[0m[36mo[0m[36md[0m[37m:[0m[37m,[0m[36mc[0m[36m:[0m[37m'[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m.[0m[37m,[0m[36mc[0m[36ml[0m[37m,[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m'[0m[36mo[0m[37m.[0m[37m [0m [37m [0m[37m,[0m[36md[0m[37m.[0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m [0m[37m.[0m[36m:[0m[36mc[0m[36m:[0m[37m,[0m[37m'[0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m.[0m[37m'[0m[37m,[0m[37m:[0m[36m:[0m[37m,[0m[37m.[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m,[0m[37m,[0m[36mx[0m[37m:[0m[36mc[0m[36ml[0m[37m.[0m[37m [0m[37m.[0m[37m;[0m[36m:[0m[36mc[0m[36mc[0m[36m:[0m[37m,[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m'[0m[36ml[0m[36m:[0m[37m [0m[37m [0m[37m [0m[37m [0m[36mc[0m[36mo[0m[37m.[0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m'[0m[37m,[0m[37m;[0m[37m;[0m[37m;[0m[37m,[0m[37m,[0m[37m'[0m[37m.[0m[37m [0m[37m [0m[37m [0m[34m.[0m[34m'[0m[34m'[0m[34m,[0m[34m,[0m[34m,[0m[37m.[0m[37m [0m[37m.[0m[36md[0m[37m:[0m[37m.[0m[36m:[0m[36ml[0m[37m;[0m[37m.[0m[37m [0m[37m [0m  [37m [0m[37m [0m[37m [0m[37m.[0m[37m'[0m[36mc[0m[36ml[0m[37m;[0m[37m.[0m[37m [0m [37m [0m[37m'[0m[36md[0m[36m:[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m [0m   [37m [0m    [37m [0m[37m [0m[37m [0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m;[0m[36mo[0m[37m'[0m[37m [0m[37m.[0m[37m,[0m[36m:[0m[36m:[0m[36mc[0m[36mc[0m[36mc[0m[36mc[0m[36mc[0m[36m:[0m[37m'[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[36ml[0m[36ml[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m.[0m[37m.[0m[37m [0m[37m [0m [37m [0m[37m [0m [37m [0m[37m [0m[34m.[0m[34m'[0m[34m'[0m[34m,[0m[34m,[0m[37m [0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m,[0m[36m:[0m[36m:[0m[37m,[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m.[0m[37m'[0m[37m:[0m[36mc[0m[36m:[0m[37m.[0m[37m [0m  [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[34m.[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m.[0m [37m [0m[37m [0m[37m [0m[37m [0m[34m.[0m[34m'[0m[34m'[0m[34m;[0m[34ml[0m[37m.[0m [37m [0m [37m [0m[37m [0m[37m [0m[37m [0m [37m [0m[37m [0m[37m [0m[37m.[0m[37m;[0m[36mc[0m[36m:[0m[36m:[0m[36mc[0m[36mc[0m[36mc[0m[36mc[0m[36mc[0m[36mc[0m[37m;[0m[37m'[0m[37m.[0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[34m.[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m'[0m[34m.[0m[37m [0m[37m [0m[37m.[0m[34m.[0m[34m'[0m[34m'[0m[34m.[0m[37m.[0m[36ml[0m[36ml[0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m [0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[34m.[0m[34m.[0m[34m.[0m[34m.[0m[34m'[0m[34m.[0m[34m.[0m[34m.[0m[34m.[0m[37m [0m[37m [0m[37m.[0m[36ml[0m[36mk[0m[36ml[0m[37m.[0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m [37m [0m[37m [0m[37m [0m [37m [0m [37m [0m[37m [0m[37m [0m[37m.[0m[36mk[0m[36mk[0m[36m:[0m[37m [0m  [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m
[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[36mc[0m[37m'[0m[37m [0m [37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m[37m [0m

Surprise! Thank you for using Flux Framework.
"""
]
