import os
from datetime import datetime

class PDFService:
    def __init__(self):
        self.pdf_dir = 'static/pdfs'
        os.makedirs(self.pdf_dir, exist_ok=True)
    
    def generate_quote_pdf(self, orcamento):
        """Gera PDF do orçamento - implementação básica por enquanto"""
        
        # Por enquanto, retorna um nome de arquivo
        # A implementação completa com WeasyPrint será feita depois
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'orcamento_{orcamento.id}_{timestamp}.pdf'
        
        # TODO: Implementar geração real do PDF com WeasyPrint
        # Por enquanto apenas simula
        
        return filename