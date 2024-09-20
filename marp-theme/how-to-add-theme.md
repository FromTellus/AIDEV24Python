# Tutorial how to add MARP theme in VS Code

This tutorial is based on the [Marp theme](https://github.com/marp-team/marp-core)
repository.

## Step 1. Create a folder for working and open the folder in VS Code

```powershell
> mkdir my-theme
> cd my-theme
> code .
```

## Step 2. Put `theme.css` in the created folder

This sets the name if the theme to "your-theme".

```css
/* @theme your-theme */

@import 'default';

h1 {
  color: red;
}
```

## Step 3. Add this to the top of a markdown file

```markdown
---
marp: true
theme: your-theme
---

# Hello, Marp
```

## Step 4. Add the theme path to VS Code settings.json

- Hit F1 and run "Preferences: Open Workspace Settings"
- Search "Themes" and find out Markdown > Marp: Themes
- Add a path theme.css. Now ready to use "your-theme"
