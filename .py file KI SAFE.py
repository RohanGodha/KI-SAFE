import tkinter as tk
from doctest import master
from tkinter import ttk
import tkinter.font as font
from tkinter import messagebox
# open dialogue box if needed
from tkinter import filedialog
import sys
import os
import subprocess
import urllib
import string
import random
import time
import webbrowser
import datetime



try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# installing the pip files

try:
    from PIL import Image, ImageTk
    import requests
    import emoji
    import pygame
    import speech_recognition as sr

# more clearer text view
except:
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                           'pillow'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                           'requests'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                           'numpy==1.19.3'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                           'emoji'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                           'pygame'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                           'SpeechRecognition'])

    # process output with an API in the subprocess module:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip',
                                    'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

    # print(installed_packages)

    from PIL import Image, ImageTk
    import requests
    import emoji
    import pygame

global cnt
pass_gen_cnt = 1

# dracula-theme
background_color = "black"
frame_colors = "#323232"
text_color = "#ff1919"


class Install_App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("KI - SAFE APP | Installation")
        self.geometry("1000x600")
        self.resizable(False, False)

        install_menu_background = background_color
        highlighted_menu_background = frame_colors
        install_menu_text = text_color
        self["background"] = install_menu_background

        def allowed_installation():
            # creating our folder to store all the multimedia and other contents
            if not os.path.exists('./KI - SAFE'):
                os.makedirs('./KI - SAFE')

            if not os.path.exists('./KI - SAFE/game'):
                os.makedirs('./KI - SAFE/game')

            # importing all the images needed for pass_manager_section from internet and storing it to the folder

            # pass-manager-png
            urllib.request.urlretrieve(
                "https://res.cloudinary.com/dewbkmgth/image/upload/v1609575151/AI_LAB_PROJECT_ASSETS/lock_wajgp9.png",
                "KI - SAFE/lock_img_cached.jpg")

            urllib.request.urlretrieve(
                "https://res.cloudinary.com/dewbkmgth/image/upload/v1610080043/ai_mst/icon_anjrbv.ico",
                "KI - SAFE/app_logo.ico")

            # pass-gen-png
            urllib.request.urlretrieve(
                "https://res.cloudinary.com/dewbkmgth/image/upload/v1609575151/AI_LAB_PROJECT_ASSETS/key_fyvykk.png",
                "KI - SAFE/pass_gen.png")

            # notes-man-png
            urllib.request.urlretrieve(
                "https://res.cloudinary.com/dewbkmgth/image/upload/v1609575151/AI_LAB_PROJECT_ASSETS/notes_fqecmo.png",
                "KI - SAFE/notes_man.png")

            time.sleep(1)

            # FACEBOOK
            urllib.request.urlretrieve(
                "https://res.cloudinary.com/dewbkmgth/image/upload/v1607101034/ai_mst/facebook_jr1ojv.png",
                "KI - SAFE/facebook_banner.png")

            # SPOTIFY
            urllib.request.urlretrieve(
                "https://b8g9x2x5.rocketcdn.me/wp-content/uploads/2018/08/spotify-logo-1920x1080_fouoik.jpg",
                "KI - SAFE/spotify_banner.jpg")

            # AMAZON
            urllib.request.urlretrieve(
                "https://images-na.ssl-images-amazon.com/images/G/01/gc/designs/livepreview/amazon_dkblue_noto_email_v2016_us-main._CB468775337_.png",
                "KI - SAFE/amazon_banner.png")

            time.sleep(1)

            # social media icons

            urllib.request.urlretrieve(
                "https://res.cloudinary.com/dewbkmgth/image/upload/v1609575151/AI_LAB_PROJECT_ASSETS/youtube_qj4kdc.png",
                "KI - SAFE/youtube_logo.png")

            urllib.request.urlretrieve(
                "https://res.cloudinary.com/dewbkmgth/image/upload/v1609575151/AI_LAB_PROJECT_ASSETS/twitter_mzwymh.png",
                "KI - SAFE/twitter_logo.png")

            urllib.request.urlretrieve(
                "https://res.cloudinary.com/dewbkmgth/image/upload/v1609575151/AI_LAB_PROJECT_ASSETS/github_j8jewq.png",
                "KI - SAFE/github_logo.png")

            urllib.request.urlretrieve(
                "https://res.cloudinary.com/dewbkmgth/image/upload/v1608275698/ai_mst/new_file_weqmsa.png",
                "KI - SAFE/new_file.png")

            time.sleep(1)

            # installation for Pyaudio
            urllib.request.urlretrieve(
                "https://res.cloudinary.com/dewbkmgth/raw/upload/v1609584458/ai_mst/PyAudio-0.2.11-cp37-cp37m-win_amd64_h93esm.whl",
                "KI - SAFE/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl")
            pyaudio_file = "KI - SAFE/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl"
            subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                                   pyaudio_file])


        def call_the_app():
            allowed_installation()
            self.destroy()
            myApp = PassKeeper()
            myApp.mainloop()

        # custom fonts
        from tkinter import font
        terms_cond_font = font.Font(name='appHighlightFontH', size=40, weight='bold')
        p_font = font.Font(family="Helvatica", name='appHighlightFontP', size=12, weight='bold')

        font.nametofont("TkDefaultFont").configure(size=20)
        font.nametofont("TkTextFont").configure(size=20)

        app_header_frame = tk.Frame(self, background=install_menu_background)
        app_header_frame.pack(side="top", fill="x", expand=True)

        # terms and condition frame
        terms_frame = tk.Frame(self, background=install_menu_background, relief=tk.SUNKEN)
        terms_frame.pack(side="top", expand=True, fill="x")

        app_name_head = ttk.Label(app_header_frame, text="KI - SAFE", font=terms_cond_font,
                                  foreground=install_menu_text,
                                  background=install_menu_background,
                                  )
        app_name_head.pack(side="top", pady=(40, 40))

        terms_label = ttk.Label(terms_frame,
                                text="K.I (Kapiushon International) - SAFE is a free to use app, but you need to agree to some Terms\n and Privacy Policy –\n\n"
                                     "\U00002794 You allow us to install the necessary packages on your system to ensure the all requirements\n     for app are satisfied.\n"
                                     "\U00002794 You shall not emulate, clone, rent, lend, lease, sell, modify, decompile, or reverse engineer\n     the Software or disassemble or create derivative works based on the Software.\n"
                                     "\U00002794 We have right to terminate Your License to use the Software in the event You breach any of\n      the terms and conditions of this Agreement.\n",
                                font=p_font, background=highlighted_menu_background, foreground=install_menu_text)
        terms_label.pack(side="top", padx=(40, 40), pady=(0, 70), expand=True, fill="x")

        user_choice_frame = tk.Frame(self, background=install_menu_background)
        user_choice_frame.pack(side="top")

        # allow and deny buttons
        allow_btn = ttk.Button(user_choice_frame, text="I Agree, Continue >", command=call_the_app,
                               style="user_choice.TButton")
        allow_btn.pack(side="left", padx=(50, 50), pady=(20, 40))

        deny_btn = ttk.Button(user_choice_frame, text="Cancel", command=self.destroy, style="user_choice.TButton")
        deny_btn.pack(side="left", padx=(50, 50), pady=(20, 40))


class PassKeeper(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("KI- SAFE APP")
        self.iconbitmap(r'./KI - SAFE/app_logo.ico')
        self.resizable(False, False)

        # creating a container
        container = tk.Frame(self)
        container.grid(sticky="NSEW")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing an empty dictionary that will store different page layouts
        self.frame = dict()

        # iterating through a for loop that assign the different page layouts
        for FrameClass in (HomePage, PassManager, PassGenerator, NotesManager):
            frame = FrameClass(container, self)
            # initializing the frames of that object from all three sections
            self.frame[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(HomePage)

    # displaying the current frame that has been passed
    def show_frame(self, container):
        frame = self.frame[container]
        frame.tkraise()


class HomePage(tk.Frame, tk.Tk):
    def __init__(self, container, controller, **kwargs):
        global gradient_background_wallpaper
        super().__init__(container, **kwargs)

        def callback(url):
            webbrowser.open_new(url)

        def call_game(x):
            game_loc = "KI - SAFE/game/game.py"
            subprocess.call(["python.exe", game_loc])

        self["background"] = background_color

        # fonts

        font.nametofont("TkDefaultFont").configure(size=20)
        font.nametofont("TkTextFont").configure(size=20)

        copy_frame = tk.Frame(self, background=background_color)
        copy_frame.pack(side="top", expand=True, fill="both")

        # three user-menu frames
        f_1 = tk.Frame(copy_frame, background=frame_colors)
        f_2 = tk.Frame(copy_frame, background=frame_colors)
        f_3 = tk.Frame(copy_frame, background=frame_colors)

        app_tagline = ttk.Label(copy_frame, text="Your data is \U0001F512 with us", background=background_color,
                                foreground=text_color, font=('Helvetica', 30, 'bold'))
        app_tagline.place(x=500, y=10)

        # packing the frames onto the screen
        f_1.pack(side="left", padx=(120, 0), pady=(140, 50))
        f_2.pack(side="left", padx=(50, 50), pady=(140, 50))
        f_3.pack(side="left", padx=(0, 100), pady=(140, 50))

        # labels for the three different frames
        label_1 = tk.Label(f_1, text="Password Manager", background=frame_colors, height=5, width=20,
                           foreground=text_color, font=("Helvitca", 20, "bold"))
        label_2 = tk.Label(f_2, text="Password Generator", background=frame_colors, height=5, width=20,
                           foreground=text_color, font=("Helvitca", 20, "bold"))
        label_3 = tk.Label(f_3, text="Notes Manager", background=frame_colors, height=5, width=20,
                           foreground=text_color, font=("Helvitca", 20, "bold"))

        # pass-man
        pass_man_img = Image.open("./KI - SAFE/lock_img_cached.jpg")
        pass_man_img = ImageTk.PhotoImage(pass_man_img)
        pass_man_lab = tk.Label(f_1, image=pass_man_img, background=frame_colors, height=300, width=300)

        pass_man_lab.image = pass_man_img
        pass_man_lab.pack(side="top")
        pass_man_lab.bind("<Button-1>", lambda e: callback("http://www.youtube.com"))

        # pass-gen
        pass_gen_img = Image.open("./KI - SAFE/pass_gen.png")
        pass_gen_img = pass_gen_img.resize((128, 128), Image.ANTIALIAS)
        pass_gen_img = ImageTk.PhotoImage(pass_gen_img)
        pass_gen_lab = tk.Label(f_2, image=pass_gen_img, background=frame_colors, height=300, width=300)

        pass_gen_lab.image = pass_gen_img
        pass_gen_lab.pack(side="top")
        pass_gen_lab.bind("<Button-1>", lambda e: callback("http://www.youtube.com"))

        # note-man
        notes_man_img = Image.open("./KI - SAFE/notes_man.png")
        notes_man_img = notes_man_img.resize((128, 128), Image.ANTIALIAS)
        notes_man_img = ImageTk.PhotoImage(notes_man_img)
        notes_man_lab = tk.Label(f_3, image=notes_man_img, background=frame_colors, height=300, width=300)

        notes_man_lab.image = notes_man_img
        notes_man_lab.pack(side="top")
        notes_man_lab.bind("<Button-1>", lambda e: callback("http://www.youtube.com"))

        # packing the frames onto the screen
        label_1.pack(side="top", padx=(0, 0), pady=(0, 0))
        label_2.pack(side="top", padx=(0, 0), pady=(0, 0))
        label_3.pack(side="top", padx=(0, 0), pady=(0, 0))

        # buttons
        btn_font = font.Font(family="Helvatica", name='appHighlightFontP', size=20, weight='bold')

        button_sec_1 = ttk.Button(f_1, text="Continue \U000027F6", command=lambda: controller.show_frame(PassManager))
        button_sec_1.pack(side="left", expand=True, fill='x')

        button_sec_2 = ttk.Button(f_2, text="Continue \U000027F6", command=lambda: controller.show_frame(PassGenerator))
        button_sec_2.pack(side="left", expand=True, fill='x')

        # button_sec_3 = ttk.Button(f_3, text="Continue \U000027F6", command=lambda: messagebox.showwarning("ERROR 404
        # :(", "Work in progress"))
        button_sec_3 = ttk.Button(f_3, text="Continue \U000027F6", command=lambda: controller.show_frame(NotesManager))

        button_sec_3.pack(side="left", expand=True, fill='x')

        game_frame = tk.Frame(self, background=background_color)
        game_frame.pack(side="top", expand=True, fill="x")

        # game_logo = Image.open("KI - SAFE/game/game_promo.jpg")
        # game_logo = game_logo.resize((1154, 196), Image.ANTIALIAS)
        # game_logo = ImageTk.PhotoImage(game_logo)
        # game_label = ttk.Label(game_frame, image=game_logo, background=background_color)
        # game_label.image = game_logo
        # game_label.pack(side="top", expand=True, fill="both", padx=(120, 0), pady=(0, 30))
        # game_label.bind("<Button-1>", call_game)

        lower_bar = tk.Frame(self, background=frame_colors)
        lower_bar.pack(side="top", expand=True, fill="x", pady=(70,0))

        tag_line = ttk.Label(lower_bar, text="We're here for you", font=("Helvetica", 20, "bold", "roman"),
                             background=frame_colors, foreground=text_color)
        tag_line.grid(row=0, column=0, padx=(50, 50))
        comment_label = ttk.Label(lower_bar, text="Follow us at: //", font=("Helvetica", 20, "bold", "italic"),
                                  background=frame_colors, foreground=text_color)
        comment_label.grid(row=0, column=1, padx=(600, 0))

        youtube_logo = Image.open("./KI - SAFE/youtube_logo.png")
        youtube_logo = youtube_logo.resize((50, 50), Image.ANTIALIAS)
        youtube_logo = ImageTk.PhotoImage(youtube_logo)
        youtube_label = ttk.Label(lower_bar, image=youtube_logo, background=frame_colors)

        youtube_label.image = youtube_logo
        youtube_label.grid(row=0, column=2, padx=(20, 20), pady=(0, 0))
        youtube_label.bind("<Button-1>", lambda e: callback("http://www.youtube.com"))

        twitter_logo = Image.open("./KI - SAFE/twitter_logo.png")
        twitter_logo = twitter_logo.resize((50, 50), Image.ANTIALIAS)
        twitter_logo = ImageTk.PhotoImage(twitter_logo)
        twitter_label = ttk.Label(lower_bar, image=twitter_logo, background=frame_colors)

        twitter_label.image = twitter_logo
        twitter_label.grid(row=0, column=3, padx=(0, 20), pady=(0, 0))
        twitter_label.bind("<Button-1>", lambda e: callback("https://twitter.com/kapiushon__"))

        github_logo = Image.open("./KI - SAFE/github_logo.png")
        github_logo = github_logo.resize((50, 50), Image.ANTIALIAS)
        github_logo = ImageTk.PhotoImage(github_logo)
        github_label = ttk.Label(lower_bar, image=github_logo, background=frame_colors)

        github_label.image = github_logo
        github_label.grid(row=0, column=4, padx=(0, 20), pady=(0, 0))
        github_label.bind("<Button-1>", lambda e: callback("https://github.com/OMEN-D/pass_manager"))


# Password Manager Section
class PassManager(ttk.Frame, tk.Tk):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        copy_frame = tk.Frame(self, background=background_color)
        copy_frame.pack(expand=True, fill="both")

        def callback(url):
            webbrowser.open_new(url)

        # a side-nav frame
        side_nav_frame = tk.Frame(copy_frame, background=frame_colors)

        side_nav_frame.grid(row=0, column=0, sticky="NS")

        logo = Image.open("./KI - SAFE/lock_img_cached.jpg")

        # resizing the image to meet our requirements
        logo = logo.resize((150, 150), Image.ANTIALIAS)

        logo = ImageTk.PhotoImage(logo)

        # creating a label to display image
        panel = ttk.Label(side_nav_frame, image=logo, background=frame_colors)

        # setting image as logo and displaying it using grid
        panel.image = logo
        panel.grid(row=0, column=0, padx=(50, 50), pady=(150, 50))

        home_button = ttk.Button(side_nav_frame, text="Home",
                                 command=lambda: controller.show_frame(HomePage)
                                 )
        home_button.grid(row=1, column=0, padx=(50, 50), pady=(50, 50), sticky="WE")

        # Navigation buttons

        pass_manager_button = ttk.Button(side_nav_frame, text="Password Manager",
                                         command=lambda: controller.show_frame(PassManager)
                                         )
        pass_manager_button.grid(row=2, column=0, padx=(50, 50), pady=(20, 20), sticky="WE")

        pass_generator_button = ttk.Button(side_nav_frame, text="Password Generator",
                                           command=lambda: controller.show_frame(PassGenerator)
                                           )
        pass_generator_button.grid(row=3, column=0, padx=(50, 50), pady=(20, 20), sticky="WE")

        notes_manager_button = ttk.Button(side_nav_frame, text="Notes Manager",
                                          command=lambda: controller.show_frame(NotesManager)
                                          )
        notes_manager_button.grid(row=4, column=0, padx=(50, 50), pady=(20, 20), sticky="WE")

        # social media icons section at the bottom
        social_media_icons_frame = tk.Frame(side_nav_frame, background=frame_colors)
        social_media_icons_frame.grid(row=5, column=0, padx=(80, 20), pady=(50, 10), sticky="W")

        youtube_logo = Image.open("./KI - SAFE/youtube_logo.png")
        youtube_logo = youtube_logo.resize((50, 50), Image.ANTIALIAS)
        youtube_logo = ImageTk.PhotoImage(youtube_logo)
        youtube_label = ttk.Label(social_media_icons_frame, image=youtube_logo, background=frame_colors)

        youtube_label.image = youtube_logo
        youtube_label.grid(row=0, column=0, padx=(20, 20), pady=(0, 0))
        youtube_label.bind("<Button-1>", lambda e: callback("http://www.youtube.com"))

        twitter_logo = Image.open("./KI - SAFE/twitter_logo.png")
        twitter_logo = twitter_logo.resize((50, 50), Image.ANTIALIAS)
        twitter_logo = ImageTk.PhotoImage(twitter_logo)
        twitter_label = ttk.Label(social_media_icons_frame, image=twitter_logo, background=frame_colors)

        twitter_label.image = twitter_logo
        twitter_label.grid(row=0, column=1, padx=(0, 20), pady=(0, 0))
        twitter_label.bind("<Button-1>", lambda e: callback("https://twitter.com/kapiushon__"))

        github_logo = Image.open("./KI - SAFE/github_logo.png")
        github_logo = github_logo.resize((50, 50), Image.ANTIALIAS)
        github_logo = ImageTk.PhotoImage(github_logo)
        github_label = ttk.Label(social_media_icons_frame, image=github_logo, background=frame_colors)

        github_label.image = github_logo
        github_label.grid(row=0, column=2, padx=(0, 20), pady=(0, 0))
        github_label.bind("<Button-1>", lambda e: callback("https://github.com/OMEN-D/pass_manager"))

        # clear user entries function
        def clear_user_entries():
            user_name_entry.delete(0, "end")
            user_pass_entry.delete(0, "end")
            url_entry.delete(0, "end")

        # storing user credentials part
        def save_data():
            global status_label
            website = url.get()
            u_name = user_name.get()
            u_pass = user_pass.get()

            if not website:
                messagebox.showwarning("Invalid or No input!", "You forgot to enter the url.")
            elif not u_name:
                messagebox.showwarning("Invalid or No input!", "You forgot to enter name.")
            elif not u_pass:
                messagebox.showwarning("Invalid or No input!", "You forgot to enter password.")
            else:
                pass

            if "facebook" in website.lower():
                # facebook frame to hold the info related to facebook
                fb_frame = tk.Frame(store_credentials_frame, background=background_color)
                fb_frame.grid(row=0, column=0, padx=(30, 30), pady=(50, 50))

                # packing the banner and user_data into the facebook frame
                # urllib.request.urlretrieve(
                #     "data:image/png;base64,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",
                #     "facebook_banner.png")

                fb_banner = Image.open("./KI - SAFE/facebook_banner.png")

                # resizing the image to meet our requirements
                fb_banner = fb_banner.resize((300, 150), Image.ANTIALIAS)

                fb_banner = ImageTk.PhotoImage(fb_banner)

                # creating a label to display image
                fb_panel = ttk.Label(fb_frame, image=fb_banner)

                # setting image as logo and displaying it using grid
                fb_panel.image = fb_banner
                fb_panel.pack(side="top")
                fb_label = ttk.Label(fb_frame, text=f"User name: {u_name}\nPassword: {u_pass}",
                                     background=background_color, foreground=text_color)
                fb_label.pack(side="top")

            if "spotify" in website.lower():
                # facebook frame to hold the info related to facebook
                spotify_frame = tk.Frame(store_credentials_frame, background=background_color)
                spotify_frame.grid(row=0, column=1, padx=(30, 30), pady=(50, 50))

                # packing the banner and user_data into the facebook frame

                spotify_banner = Image.open("KI - SAFE/spotify_banner.jpg")

                # resizing the image to meet our requirements
                spotify_banner = spotify_banner.resize((300, 150), Image.ANTIALIAS)

                spotify_banner = ImageTk.PhotoImage(spotify_banner)

                # creating a label to display image
                spotify_panel = ttk.Label(spotify_frame, image=spotify_banner)

                # setting image as logo and displaying it using grid
                spotify_panel.image = spotify_banner
                spotify_panel.pack(side="top")
                spotify_label = ttk.Label(spotify_frame, text=f"User name: {u_name}\nPassword: {u_pass}",
                                          background=background_color, foreground=text_color)
                spotify_label.pack(side="top")

            if "amazon" in website.lower():
                # facebook frame to hold the info related to facebook
                amazon_frame = tk.Frame(store_credentials_frame, background=background_color)
                amazon_frame.grid(row=0, column=2, padx=(30, 30), pady=(50, 50))

                # packing the banner and user_data into the facebook frame

                amazon_banner = Image.open("KI - SAFE/amazon_banner.png")

                # resizing the image to meet our requirements
                amazon_banner = amazon_banner.resize((300, 150), Image.ANTIALIAS)

                amazon_banner = ImageTk.PhotoImage(amazon_banner)

                # creating a label to display image
                amazon_panel = ttk.Label(amazon_frame, image=amazon_banner)

                # setting image as logo and displaying it using grid
                amazon_panel.image = amazon_banner
                amazon_panel.pack(side="top")
                amazon_label = ttk.Label(amazon_frame, text=f"User name: {u_name}\nPassword: {u_pass}",
                                         background=background_color, foreground=text_color)
                amazon_label.pack(side="top")

            return True

        # creating another frame, so we can easily manage UI
        user_data_frame = tk.Frame(copy_frame, background=background_color)
        user_data_frame.grid(row=0, column=1, sticky="N", padx=(200, 0), pady=(30, 30))

        # initializing the variables
        url = tk.StringVar()
        user_name = tk.StringVar()
        user_pass = tk.StringVar()
        status = tk.StringVar()

        # defining entry fields
        url_prompt = ttk.Label(user_data_frame, text="Website:", justify="left", background=background_color,
                               foreground=text_color)
        user_name_prompt = ttk.Label(user_data_frame, text="Name:", justify="left", background=background_color,
                                     foreground=text_color)
        user_pass_prompt = ttk.Label(user_data_frame, text="Password:", justify="right", background=background_color,
                                     foreground=text_color)

        url_entry = ttk.Entry(user_data_frame, textvariable=url)
        user_name_entry = ttk.Entry(user_data_frame, textvariable=user_name)
        user_pass_entry = ttk.Entry(user_data_frame, textvariable=user_pass)

        # new button that resets the previous entries
        reset_new_user_btn = ttk.Button(user_data_frame, text="New entry", command=clear_user_entries)
        reset_new_user_btn.grid(row=4, column=0, padx=(50, 50), pady=(20, 0))

        # displaying all the labels and entry fields
        url_prompt.grid(row=0, column=0, pady=(15, 15), sticky="W")
        user_name_prompt.grid(row=1, column=0, pady=(15, 15), sticky="W")
        user_pass_prompt.grid(row=2, column=0, pady=(15, 15), sticky="W")

        url_entry.grid(row=0, column=1, pady=(15, 15), padx=(10, 0))
        url_entry.focus()
        user_name_entry.grid(row=1, column=1, pady=(15, 15), padx=(10, 0))
        user_name_entry.focus()
        user_pass_entry.grid(row=2, column=1, pady=(15, 15), padx=(10, 0))
        user_pass_entry.focus()
        # status.grid(row=3, column=0, columnspan=3)

        # save button
        save_button = ttk.Button(user_data_frame, text="Save", command=save_data)
        save_button.grid(row=4, column=1, pady=(20, 0), padx=(50, 50), sticky="W")

        # stored credentials

        # a separate frame for the passwords display section
        store_credentials_frame = tk.Frame(copy_frame, background=background_color)
        store_credentials_frame.grid(row=0, column=1, pady=(350, 0), padx=(0, 0), sticky="W")
        # store_credentials_frame.place(x=400, y=450)


class PassGenerator(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)

        slight_dark_bg = frame_colors

        u_name_var = tk.StringVar()
        u_id_var = tk.StringVar()
        u_pass_var = tk.StringVar()

        copy_frame = tk.Frame(self, background=background_color)
        copy_frame.pack(expand=True, fill="both")

        def callback(url):
            webbrowser.open_new(url)

        # here we are using same code for side-navigation menu to make the GUI consistent

        def show_credentials():
            if pass_gen_cnt == 1:
                # differnet pass and creds generation
                diff_pass_gen_btn = ttk.Button(pass_generator_frame, text="Next", command=diff_pass_creds)
                diff_pass_gen_btn.place(x=772, y=130)
            else:
                pass

            username = u_name_var.get()
            if not username:
                messagebox.showwarning("Invalid or No input!", "Please enter your name.")
            else:
                pass
            s1 = string.ascii_lowercase
            # print(s1)
            s2 = string.ascii_uppercase
            # print(s2)
            s3 = string.digits
            # print(s3)
            s4 = ["@", "#", "$", "%", "&"]
            # print(s4)
            len = random.randint(8, 12)
            # print(len)
            s = []
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(s4)
            # print(s)
            random.shuffle(s)
            # print(s)
            self.password = "".join(s[0:len])
            # print(password)
            num = random.randint(0, 999999)
            self.email = username + '@' + str(num)
            global pass_gen_pass
            global pass_gen_id

            if not username:
                self.email = ""
                self.password = ""
            pass_gen_id = ttk.Label(pass_generator_frame, text=self.email, background=background_color,
                                    foreground=text_color)
            pass_gen_pass = ttk.Label(pass_generator_frame, text=self.password, background=background_color,
                                      foreground=text_color)

            pass_gen_id.grid(row=2, column=1, pady=(15, 15), padx=(10, 0))
            pass_gen_pass.grid(row=3, column=1, pady=(15, 15), padx=(10, 0))

        def diff_pass_creds():
            pass_gen_pass.destroy()
            pass_gen_id.destroy()
            show_credentials()

        # a side-nav frame
        side_nav_frame = tk.Frame(copy_frame, background=frame_colors)
        tk.Grid.rowconfigure(side_nav_frame, 0, weight=1)
        tk.Grid.columnconfigure(side_nav_frame, 0, weight=1)

        side_nav_frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)

        logo = Image.open("./KI - SAFE/pass_gen.png")

        # resizing the image to meet our requirements
        logo = logo.resize((150, 150), Image.ANTIALIAS)

        logo = ImageTk.PhotoImage(logo)

        # creating a label to display image
        panel = ttk.Label(side_nav_frame, image=logo, background=frame_colors)

        # setting image as logo and displaying it using grid
        panel.image = logo
        panel.grid(row=0, column=0, padx=(50, 50), pady=(150, 50))

        home_button = ttk.Button(side_nav_frame, text="Home",
                                 command=lambda: controller.show_frame(HomePage)
                                 )
        home_button.grid(row=1, column=0, padx=(50, 50), pady=(50, 50), sticky="WE")

        # Navigation buttons

        pass_manager_button = ttk.Button(side_nav_frame, text="Password Manager",
                                         command=lambda: controller.show_frame(PassManager)
                                         )
        pass_manager_button.grid(row=2, column=0, padx=(50, 50), pady=(20, 20), sticky="WE")

        pass_generator_button = ttk.Button(side_nav_frame, text="Password Generator",
                                           command=lambda: controller.show_frame(PassGenerator)
                                           )
        pass_generator_button.grid(row=3, column=0, padx=(50, 50), pady=(20, 20), sticky="WE")

        notes_manager_button = ttk.Button(side_nav_frame, text="Notes Manager",
                                          command=lambda: controller.show_frame(NotesManager)
                                          )
        notes_manager_button.grid(row=4, column=0, padx=(50, 50), pady=(20, 20), sticky="WE")

        # social media icons section at the bottom
        social_media_icons_frame = tk.Frame(side_nav_frame, background=frame_colors)
        social_media_icons_frame.grid(row=5, column=0, padx=(80, 20), pady=(50, 10), sticky="W")

        youtube_logo = Image.open("./KI - SAFE/youtube_logo.png")
        youtube_logo = youtube_logo.resize((50, 50), Image.ANTIALIAS)
        youtube_logo = ImageTk.PhotoImage(youtube_logo)
        youtube_label = ttk.Label(social_media_icons_frame, image=youtube_logo, background=frame_colors)

        youtube_label.image = youtube_logo
        youtube_label.grid(row=0, column=0, padx=(20, 20), pady=(0, 0))
        youtube_label.bind("<Button-1>", lambda e: callback("http://www.youtube.com"))

        twitter_logo = Image.open("./KI - SAFE/twitter_logo.png")
        twitter_logo = twitter_logo.resize((50, 50), Image.ANTIALIAS)
        twitter_logo = ImageTk.PhotoImage(twitter_logo)
        twitter_label = ttk.Label(social_media_icons_frame, image=twitter_logo, background=frame_colors)

        twitter_label.image = twitter_logo
        twitter_label.grid(row=0, column=1, padx=(0, 20), pady=(0, 0))
        twitter_label.bind("<Button-1>", lambda e: callback("https://twitter.com/kapiushon__"))

        github_logo = Image.open("./KI - SAFE/github_logo.png")
        github_logo = github_logo.resize((50, 50), Image.ANTIALIAS)
        github_logo = ImageTk.PhotoImage(github_logo)
        github_label = ttk.Label(social_media_icons_frame, image=github_logo, background=frame_colors)

        github_label.image = github_logo
        github_label.grid(row=0, column=2, padx=(0, 20), pady=(0, 0))
        github_label.bind("<Button-1>", lambda e: callback("https://github.com/OMEN-D/pass_manager"))

        # pass generator

        # new frame for pass generator
        pass_generator_frame = tk.Frame(copy_frame, background=background_color)
        pass_generator_frame.grid(row=0, column=1, stick=tk.N + tk.S + tk.E + tk.W, padx=(0, 0))

        # defining entry fields

        user_name_pass_gen = ttk.Label(pass_generator_frame, text="Name:", justify="left", background=background_color,
                                       foreground=text_color)
        pass_gen_u_id_prompt = ttk.Label(pass_generator_frame, text="User ID:", justify="left",
                                         background=background_color, foreground=text_color)
        pass_gen_u_pass_prompt = ttk.Label(pass_generator_frame, text="Password:", justify="right",
                                           background=background_color, foreground=text_color)

        pass_gen_name = ttk.Entry(pass_generator_frame, textvariable=u_name_var)

        # displaying all the labels and entry fields
        user_name_pass_gen.grid(row=1, column=0, pady=(30, 15), sticky="W", padx=(200, 0))
        pass_gen_u_id_prompt.grid(row=2, column=0, pady=(15, 15), sticky="W", padx=(200, 0))
        pass_gen_u_pass_prompt.grid(row=3, column=0, pady=(15, 15), sticky="W", padx=(200, 0))

        pass_gen_name.grid(row=1, column=1, pady=(40, 15), padx=(10, 0))
        pass_gen_name.focus()

        # a button that generates the passwords and user id and display them onto the screen

        pass_gen_btn = ttk.Button(pass_generator_frame, text="Generate", command=show_credentials)
        pass_gen_btn.grid(row=1, column=2, padx=(50, 120), pady=(30, 0))

        #
        # a new frame what we recommend

        tips_pass_gen_sec = tk.Frame(self, background=slight_dark_bg)
        tips_pass_gen_sec.place(x=430, y=330)

        pass_gen_tip_1 = ttk.Label(tips_pass_gen_sec,
                                   text="1. Longer passwords are better: 8 characters is a starting point",
                                   background=slight_dark_bg, foreground=text_color)
        pass_gen_tip_1.grid(row=0, column=0, padx=(10, 10), pady=(50, 50), sticky="W")

        pass_gen_tip_2 = ttk.Label(tips_pass_gen_sec, text="2. Don't recycle your passwords", background=slight_dark_bg,
                                   foreground=text_color)
        pass_gen_tip_2.grid(row=1, column=0, padx=(10, 10), pady=(0, 50), sticky="W")

        pass_gen_tip_3 = ttk.Label(tips_pass_gen_sec,
                                   text="3. Avoid common words and character combinations in your password",
                                   background=slight_dark_bg, foreground=text_color)
        pass_gen_tip_3.grid(row=2, column=0, padx=(10, 10), pady=(0, 50), sticky="W")

        pass_gen_tip_4 = ttk.Label(tips_pass_gen_sec, text="4. Use a password manager to keep track of your passwords",
                                   background=slight_dark_bg, foreground=text_color)
        pass_gen_tip_4.grid(row=3, column=0, padx=(10, 10), pady=(0, 75), sticky="W")


class NotesManager(tk.Frame, tk.Tk):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.l_files = []

        global file_cnt
        file_cnt = 1
        global file_list
        file_list = list()

        style = ttk.Style(self)
        style.configure('TButton', font=
        ('Helvetica', 20, 'normal'),
                        borderwidth='4')

        def callback(url):
            webbrowser.open_new(url)

        # Changes will be reflected
        # by the movement of mouse.
        style.map('TButton', foreground=[('active', '!disabled', frame_colors)],
                  background=[('active', 'red')])

        self["background"] = background_color

        def catalog():
            file_list = []
            Path = "KI - SAFE/files/"
            filelist = os.listdir(Path)
            for i in filelist:
                if i.endswith(".txt") and i != 'test.txt':
                    file_list.append(i)
            backup = file_list
            file_list = []
            return ui(backup)

        def open_file(file_loc):
            subprocess.call(["notepad.exe", file_loc])

        def ui(l):
            dates_times = datetime.datetime.now()
            print(l)
            file_loc = "KI - SAFE/files/" + l
            a = ttk.Label(banner_frame, text="\U00002022  " + l + f"\t  {dates_times}", background=background_color,
                          foreground=text_color, anchor="w")
            a.pack(side="top", padx=(0, 0))
            a.bind("<Button-1>", lambda e: open_file(file_loc))

        def new_file_func():
            global temp_file
            new_window = tk.Toplevel(master)
            new_window.title("Notes Manager")
            new_window.geometry("1200x700")
            new_window.resizable(False, False)

            # frame 1 for the save and file name options
            new_win_controls = tk.Frame(new_window, background=frame_colors)
            new_win_controls.grid(row=0, column=0, sticky="ns")
            global f_name, file_cnt
            f_name = tk.StringVar()
            f_title = tk.StringVar()
            text_file = tk.StringVar()

            file_name_label = ttk.Label(new_win_controls, text="Filename:", background=frame_colors,
                                        foreground=text_color)
            file_title_label = ttk.Label(new_win_controls, text="Title:", background=frame_colors,
                                         foreground=text_color)
            self.file_name = ttk.Entry(new_win_controls, textvariable=f_name, width=10, background=frame_colors,
                                       foreground=background_color)
            file_title = ttk.Entry(new_win_controls, textvariable=f_title, width=10, background=frame_colors,
                                   foreground=background_color)

            file_name_label.grid(row=0, column=0, pady=(20, 20), padx=(15, 20), sticky="W")
            file_title_label.grid(row=1, column=0, pady=(20, 20), padx=(15, 20), sticky="W")
            self.file_name.grid(row=0, column=1, sticky="W", pady=(20, 20), padx=(0, 50))
            file_title.grid(row=1, column=1, sticky="W", pady=(20, 20), padx=(0, 50))

            # frame 2 for the input text_box and the scrollbar
            new_win_content = ttk.Frame(new_window)
            new_win_content.grid(row=0, column=1)

            # new_window.resizable(False, False)
            new_window.title("Notes Manager")

            text_box = tk.Text(new_win_content, height=35, width=70)
            text_box.grid(row=0, column=0)

            def retrieve_input():
                inputValue = text_box.get("1.0", "end-1c")
                print(f_name)
                temp_file = self.file_name.get()
                with open("KI - SAFE/files/" + self.file_name.get() + '.txt', 'w') as writer:
                    writer.write(inputValue)
                self.l_files.append(self.file_name.get())
                new_window.destroy()
                ui(temp_file)

            def speech_txt_func():
                import speech_recognition as sr
                r = sr.Recognizer()
                mic = sr.Microphone()
                with mic as source:
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)

                r.recognize_google(audio)

                # setting up the response object
                response = {
                    "success": True,
                    "error": None,
                    "transcription": None
                }

                # try recognizing the speech if there is any error response will be displayed accordingly
                try:
                    response["transcription"] = r.recognize_google(audio)
                    text_box.insert(tk.INSERT, "" +response["transcription"] + " ")
                except sr.RequestError:
                    # API was unreachable or unresponsive
                    response["success"] = False
                    response["error"] = "API unavailable"
                    messagebox.showwarning("ERROR!", "Service Unavailable/Unreachable/Unintelligent audio match.")
                except sr.UnknownValueError:
                    # speech was unintelligible
                    response["error"] = "Unable to recognize speech"
                    messagebox.showwarning("ERROR!", "Service Unavailable/Unreachable/Unintelligent audio match.")
                return response

            use_speech_to_text = ttk.Button(new_win_controls, text="Use speech to text", command=speech_txt_func)
            use_speech_to_text.place(x=50, y=250)
            # label to display the voice instructions
            voice_istrc = ttk.Label(new_win_controls, text="Wait 1 second\nbefore speaking.", background=frame_colors, foreground=text_color)

            voice_istrc.place(x=70, y=300)
            file_save_btn = ttk.Button(new_win_controls, text="Save & Close", command=retrieve_input)
            file_save_btn.place(x=70, y=400)

            text_scroll = ttk.Scrollbar(new_win_content, orient="vertical", command=text_box.yview)
            text_scroll.grid(row=0, column=1, sticky="ns")
            text_box["yscrollcommand"] = text_scroll.set

        # a side-nav frame
        side_nav_frame = tk.Frame(self, background=frame_colors)

        side_nav_frame.grid(row=0, column=0, sticky="NS")

        logo = Image.open("KI - SAFE/notes_man.png")

        # resizing the image to meet our requirements
        logo = logo.resize((150, 150), Image.ANTIALIAS)

        logo = ImageTk.PhotoImage(logo)

        # creating a label to display image
        panel = ttk.Label(side_nav_frame, image=logo, background=frame_colors)

        # setting image as logo and displaying it using grid
        panel.image = logo
        panel.grid(row=0, column=0, padx=(50, 50), pady=(150, 50))

        home_button = ttk.Button(side_nav_frame, text="Home",
                                 command=lambda: controller.show_frame(HomePage)
                                 )
        home_button.grid(row=1, column=0, padx=(50, 50), pady=(50, 50), sticky="WE")

        # Navigation buttons

        pass_manager_button = ttk.Button(side_nav_frame, text="Password Manager",
                                         command=lambda: controller.show_frame(PassManager)
                                         )
        pass_manager_button.grid(row=2, column=0, padx=(50, 50), pady=(20, 20), sticky="WE")

        pass_generator_button = ttk.Button(side_nav_frame, text="Password Generator",
                                           command=lambda: controller.show_frame(PassGenerator)
                                           )
        pass_generator_button.grid(row=3, column=0, padx=(50, 50), pady=(20, 20), sticky="WE")

        notes_manager_button = ttk.Button(side_nav_frame, text="Notes Manager",
                                          command=lambda: controller.show_frame(NotesManager)
                                          )
        notes_manager_button.grid(row=4, column=0, padx=(50, 50), pady=(20, 20), sticky="WE")

        # social media icons section at the bottom
        social_media_icons_frame = tk.Frame(side_nav_frame, background=frame_colors)
        social_media_icons_frame.grid(row=5, column=0, padx=(80, 20), pady=(50, 10), sticky="W")

        youtube_logo = Image.open("./KI - SAFE/youtube_logo.png")
        youtube_logo = youtube_logo.resize((50, 50), Image.ANTIALIAS)
        youtube_logo = ImageTk.PhotoImage(youtube_logo)
        youtube_label = ttk.Label(social_media_icons_frame, image=youtube_logo, background=frame_colors)

        youtube_label.image = youtube_logo
        youtube_label.grid(row=0, column=0, padx=(20, 20), pady=(0, 0))
        youtube_label.bind("<Button-1>", lambda e: callback("http://www.youtube.com"))

        twitter_logo = Image.open("./KI - SAFE/twitter_logo.png")
        twitter_logo = twitter_logo.resize((50, 50), Image.ANTIALIAS)
        twitter_logo = ImageTk.PhotoImage(twitter_logo)
        twitter_label = ttk.Label(social_media_icons_frame, image=twitter_logo, background=frame_colors)

        twitter_label.image = twitter_logo
        twitter_label.grid(row=0, column=1, padx=(0, 20), pady=(0, 0))
        twitter_label.bind("<Button-1>", lambda e: callback("https://twitter.com/kapiushon__"))

        github_logo = Image.open("./KI - SAFE/github_logo.png")
        github_logo = github_logo.resize((50, 50), Image.ANTIALIAS)
        github_logo = ImageTk.PhotoImage(github_logo)
        github_label = ttk.Label(social_media_icons_frame, image=github_logo, background=frame_colors)

        github_label.image = github_logo
        github_label.grid(row=0, column=2, padx=(0, 20), pady=(0, 0))
        github_label.bind("<Button-1>", lambda e: callback("https://github.com/OMEN-D/pass_manager"))

        banner_frame = tk.Frame(self, background=background_color)
        banner_frame.grid(row=0, column=1, sticky="N", padx=(150, 50), pady=(50, 0))

        slogan = ttk.Label(banner_frame, text="YOUR SAVED NOTES WILL SHOW HERE", background=background_color,
                           foreground=text_color, font=('Helvetica', 25, 'normal', 'italic'))
        slogan.pack(side="top", pady=(0, 100))

        # # saved files
        # note_manager_frame = ttk.Frame(self)
        # note_manager_frame.grid(row=1, column=1)
        # cnt = 0
        # print(self.l_files)
        # for f in self.l_files:
        #     ttk.Label(note_manager_frame, text=f).grid(row=cnt, column=0)

        # p = ttk.Label(banner_frame, text="1. this is something random")
        # p.pack(side="left")

        if not os.path.exists("KI - SAFE/files/"):
            os.makedirs("KI - SAFE/files/")
        with open('KI - SAFE/files/test.txt', 'w') as demo:
            demo.write("Basic test file.")

        new_file_btn = ttk.Button(self, text="New file", command=new_file_func)
        new_file_btn.place(x=1200, y=680)


if not os.path.exists('./KI - SAFE'):
    app = Install_App()
    app.mainloop()
else:
    app = PassKeeper()
    app.mainloop()
