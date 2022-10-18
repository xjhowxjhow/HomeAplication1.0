

class Category:

    def _saidas():
        return ['Energia','Gás','Água','Luz','Telefone','Internet','Boletos','Servicos','Aluguel','Impostos','Veiculos','IPVA','IPTU','Esgoto','Outros']
    
    def _entradas():
        return ['Salario','Rendimentos','Beneficios','Criptomoedas','Investimentos','Cheques','Transferencia','Depositos','Pagamentos','Bolsa','Vendas','Outros']
    
    def patch_icons(icon):
        
        if icon == 'Energia':
            return ':/category_main/category_main/luz.png'
        elif icon == 'Gás':
            return ':/category_main/category_main/gas.png'
        elif icon == 'Água':
            return ':/category_main/category_main/agua.png'
        elif icon == 'Luz':
            return ':/category_main/category_main/luz.png'
        elif icon == 'Telefone':
            return ':/category_main/category_main/telefone.png'
        elif icon == 'Internet':
            return ':/category_main/category_main/internet.png'
        elif icon == 'Boletos':
            return ':/category_main/category_main/boleto.png'
        elif icon == 'Servicos':
            return ':/category_main/category_main/servicos.png'
        elif icon == 'Aluguel':
            return ':/category_main/category_main/aluguel.png'
        elif icon == 'Impostos':
            return ':/category_main/category_main/impostos.png'
        elif icon == 'Veiculos':
            return ':/category_main/category_main/veiculos.png'
        elif icon == 'IPVA':
            return ':/category_main/category_main/IPVA.png'
        elif icon == 'IPTU':
            return ':/category_main/category_main/IPTU.png'
        elif icon == 'Esgoto':
                return ':/category_main/category_main/esgoto.png'
        elif icon == 'Outros':
            return ':/category_main/category_main/outros.png'
        elif icon == 'Salario':
            return ':/category_main/category_main/salario.png'
        elif icon == 'Rendimentos':
            return ':/category_main/category_main/rendimentos.png'
        elif icon == 'Beneficios':
            return ':/category_main/category_main/beneficios.png'
        elif icon == 'Criptomoedas':
            return ':/category_main/category_main/criptomoedas.png'
        elif icon == 'Investimentos':
            return ':/category_main/category_main/investimentos.png'
        elif icon == 'Cheques':
            return ':/category_main/category_main/cheques.png'
        elif icon == 'Transferencia':
            return ':/category_main/category_main/transferencias.png'
        elif icon == 'Depositos':
            return ':/category_main/category_main/depositos.png'
        elif icon == 'Pagamentos':
            return ':/category_main/category_main/pagamentos.png'
        elif icon == 'Bolsa':
            return ':/category_main/category_main/bolsa.png'
        elif icon == 'Vendas':
            return ':/category_main/category_main/vendas.png'


class Payments_Type:
    
    def _entradas():
        return ['Credito em Conta','Dinheiro','Transferência','Cheque','Outros','Rendimentos','Criptomoedas','Pix']
    
    def _saidas():
        return ['Debito em Conta','Dinheiro','Transferência','Cheque','Outros','Pix']



class Texts_Erros:
    
    def deletar_fatura_no_menu():
        return "ATENÇÃO: Não é possivel deletar uma fatura por este meio.\n\nPara deletar uma fatura, vá na Aba Cartoes e delete pelo Extrato"
    def deletar_cartao_config():
        return "ATENÇÃO: Não é possivel deletar um cartão por este meio.\n\nPois o mesmo possui conta bancaria ativa.\n\nPara deletar este cartão vá para: \n Inicio>Contas bancarias no campo alterar"