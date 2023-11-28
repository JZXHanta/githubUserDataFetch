import requests
import flet as ft


def main(page: ft.Page):
    def button_clicked(e):
        profile_response = requests.get(
            f"https://api.github.com/users/{username_input.value}"
        )
        profile_data = (
            profile_response.json()
            if profile_response.status_code < 300
            else "That didn't work..."
        )
        repo_response = requests.get(
            f"https://api.github.com/users/{username_input.value}/repos"
        )
        repo_data = (
            repo_response.json()
            if profile_response.status_code < 300
            else "That didn't work..."
        )
        lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        try:
            for repo in repo_data:
                repo_name = repo["name"]
                languages_response = requests.get(
                    f"https://api.github.com/repos/{username_input.value}/{repo_name}/languages"
                )
                languages = languages_response.json()
                langs = ""

                for lang in languages:
                    # TODO: Figure out how to get rid of the trailing comma on last item when your brain is working
                    langs += f"{lang}, " if len(languages) > 1 else f" {lang}"
                lv.controls.append(ft.Text(f"{repo_name} - {langs}"))
        except Exception:
            lv.controls.append("Rate limit exceeded)")
            raise Exception("Rate limit exceeded")

        username = profile_data["login"]
        avatar_url = profile_data["avatar_url"]
        html_url = profile_data["html_url"]
        name = profile_data["name"]
        gh_username = ft.Text(size=100, value=username)
        gh_name = ft.Text(value=f"Name:   {name}")
        gh_link = ft.Text(value=f"Github Page:   {html_url}")
        public_repos = ft.Text(value="Public Repositories:")
        divider = ft.Divider()
        gh_avatar = ft.Image(
            src=avatar_url,
            width=150,
            height=150,
            border_radius=100,
            fit=ft.ImageFit.CONTAIN,
        )
        # Removes input data that is no longer required and updates the page
        page.remove(username_input)
        page.remove(b)
        basics_row = ft.Row(
            spacing=100,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[gh_avatar, gh_username],
        )
        page.add(basics_row)
        page.add(divider)
        st = ft.Stack(
            [
                ft.Column(
                    [
                        gh_name,
                        gh_link,
                        public_repositories,
                        lv,
                    ]
                )
            ],
            width=800,
            height=800,
        )
        page.add(st)
        page.add(gh_link)
        page.update()

    page.padding = 50
    username_input = ft.TextField(label="GH Username")
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(username_input, b)


ft.app(target=main)
