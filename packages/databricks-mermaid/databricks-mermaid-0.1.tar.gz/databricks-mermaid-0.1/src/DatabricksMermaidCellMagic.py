from IPython.core.magic import (Magics, magics_class, line_magic, cell_magic)

@magics_class
class DatabricksMermaidCellMagic(Magics):

    @cell_magic
    def mermaid(self, line: str, cell: str) -> None:
        """
        inspired from https://github.com/oruelle/md_mermaid;
        """
        displayHTML(
            f"""
            <script src='https://cdnjs.cloudflare.com/ajax/libs/mermaid/9.3.0/mermaid.min.js'></script>
            <div class="mermaid">
            {cell}
            </div>
            """ +
            """
            <script>
            function initializeMermaid() {
                mermaid.initialize({startOnLoad:true})
            }
            if (document.readyState === "complete" || document.readyState === "interactive") {
                setTimeout(initializeMermaid, 1);
            } else {
                document.addEventListener("DOMContentLoaded", initializeMermaid);
            }
            </script>
            """
        )
        return None