return {
    {
        "bjarneo/aether.nvim",
        name = "aether",
        priority = 1000,
        opts = {
            disable_italics = false,
            colors = {
                -- Monotone shades (base00-base07)
                base00 = "#0E0B09", -- Default background
                base01 = "#8c7c71", -- Lighter background (status bars)
                base02 = "#0E0B09", -- Selection background
                base03 = "#8c7c71", -- Comments, invisibles
                base04 = "#DCD5CB", -- Dark foreground
                base05 = "#ffffff", -- Default foreground
                base06 = "#ffffff", -- Light foreground
                base07 = "#DCD5CB", -- Light background

                -- Accent colors (base08-base0F)
                base08 = "#ea3e44", -- Variables, errors, red
                base09 = "#f88c90", -- Integers, constants, orange
                base0A = "#C4BAAD", -- Classes, types, yellow
                base0B = "#72c5bd", -- Strings, green
                base0C = "#a7c2cd", -- Support, regex, cyan
                base0D = "#BBBCC2", -- Functions, keywords, blue
                base0E = "#b7aeb5", -- Keywords, storage, magenta
                base0F = "#ebe7e2", -- Deprecated, brown/yellow
            },
        },
        config = function(_, opts)
            require("aether").setup(opts)
            vim.cmd.colorscheme("aether")

            -- Enable hot reload
            require("aether.hotreload").setup()
        end,
    },
    {
        "LazyVim/LazyVim",
        opts = {
            colorscheme = "aether",
        },
    },
}
