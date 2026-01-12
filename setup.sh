# Create folder for Streamlit config
mkdir -p ~/.streamlit/
# Create config.toml with proper settings
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
