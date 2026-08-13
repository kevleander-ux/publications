# What to do here

If you type a "." (period) it'll open an editor right in your browser. It takes a few seconds longer than you think it should.

You can then navigate (on the left sidebar) to `docs` to find the file you want to change. You should then be able to edit it and when you're done, command-S should save, and then you can click the little icon with three circles and, probably a blue circle with a number in it. From there click the "+" ("Stage Changes"), and then "commit & push". A few minutes later (you can check by clicking the "actions" tab at the top), the changes will be deployed

# What to do on your own computer

It's much the same, though you'll use [VS Code](https://code.visualstudio.com/download?_exp_download=fb315fc982) on your mac. You can also do
`bundle exec jekyll serve --source docs` (as it says below) in a terminal in the browser (you'll need to hunt the menus to find the terminal). Once that is running, you'll see a link like

    Server address: http://127.0.0.1:4000/

and you can go there and see the test/development version in your browser.

# stuff AI says to try

main — README updated with local serve instructions and skin guide

mm-skin — one line change in \_config.yml (minimal_mistakes_skin: "mint"). To preview: bundle exec jekyll serve --source docs on that branch.

just-the-docs — theme swapped, all pages updated with nav_order for sidebar navigation, Gemfile updated.

To preview any branch locally, just git checkout <branch-name> then bundle install && bundle exec jekyll serve --source docs. When Kevin picks one, you merge it to main and that's what
GitHub Pages will publish.
