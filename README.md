<!-- about st.markdown -->
streamlit.markdown(body: str, unsafe_allow_html: bool = False) -> 'DeltaGenerator'
Display string formatted as Markdown.

Parameters
----------
body : str
    The string to display as Github-flavored Markdown. Syntax
    information can be found at: https://github.github.com/gfm.

    This also supports:

    * Emoji shortcodes, such as ``:+1:``  and ``:sunglasses:``.
      For a list of all supported codes,
      see https://share.streamlit.io/streamlit/emoji-shortcodes.

    * LaTeX expressions, by wrapping them in "$" or "$$" (the "$$"
      must be on their own lines). Supported LaTeX functions are listed
      at https://katex.org/docs/supported.html.

unsafe_allow_html : bool
    By default, any HTML tags found in the body will be escaped and
    therefore treated as pure text. This behavior may be turned off by
    setting this argument to True.

    That said, we *strongly advise against it*. It is hard to write
    secure HTML, so by using this argument you may be compromising your
    users' security. For more information, see:

    https://github.com/streamlit/streamlit/issues/152

    *Also note that ``unsafe_allow_html`` is a temporary measure and may
    be removed from Streamlit at any time.*

    If you decide to turn on HTML anyway, we ask you to please tell us
    your exact use case here:

    https://discuss.streamlit.io/t/96

    This will help us come up with safe APIs that allow you to do what
    you want.

Example
-------
>>> st.markdown('Streamlit is **_really_ cool**.')