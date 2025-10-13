import pandas as pd
import os

# Intenta importar la librería WeasyPrint
try:
    from weasyprint import HTML
except ImportError:
    print("La librería WeasyPrint no está instalada.")
    print("Por favor, instala WeasyPrint ejecutando el siguiente comando:")
    print("pip install WeasyPrint")
    exit()

def generar_boletas_desde_csv(csv_filepath, output_dir='boletas_generadas'):
    """
    Lee un archivo CSV con datos de boletas y genera un archivo PDF
    para cada boleta con el formato deseado.

    Args:
        csv_filepath (str): La ruta al archivo CSV.
        output_dir (str): Directorio donde se guardarán los archivos PDF.
    """
    
    # Asegurarse de que el directorio de salida existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # Leer el archivo CSV usando pandas. El delimitador es punto y coma.
        df = pd.read_csv(csv_filepath, sep=';')
    except FileNotFoundError:
        print(f"Error: El archivo '{csv_filepath}' no fue encontrado.")
        return
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo CSV: {e}")
        return

    # Iterar sobre cada fila del DataFrame (cada boleta)
    for index, boleta in df.iterrows():
        # Concatenar el RUT y el dígito verificador
        rut_completo = f"{boleta['RUT_TERC']}-{boleta['DV_TERC']}"
        
        # Formatear los números con separador de miles
        def format_number(num):
            if pd.isna(num):
                return '0'
            # Convertir a entero para eliminar decimales antes de formatear
            return f"{int(num):,}".replace(",", ".")
            
        # Generar un código de barras simulado
        codigo_barras = f"7697672700{str(boleta['NUMBOL']).zfill(6)}68F7ACF"

        # Plantilla HTML con f-string para insertar los datos de la boleta
        html_template = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Boleta de Prestación de Servicios N°{boleta['NUMBOL']}</title>
            <script src="https://cdn.tailwindcss.com"></script>
            <style>
                body {{
                    font-family: 'Inter', sans-serif;
                    background-color: #f3f4f6;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    padding: 2rem;
                }}
                .barcode {{
                    font-family: 'Libre Barcode 39', cursive;
                }}
                @import url('https://fonts.googleapis.com/css2?family=Libre+Barcode+39&display=swap');
            </style>
        </head>
        <body class="bg-gray-100">
            <div class="w-full max-w-4xl p-8 bg-white border border-gray-300 rounded-lg shadow-xl">
                <div class="flex justify-between items-start mb-6 border-b border-gray-400 pb-4">
                    <div class="text-left w-1/2 pr-4">
                        <p class="font-bold text-sm">{boleta['NOMBRE']}</p>
                        <p class="text-xs">RUT: {boleta['RUT_TERC']}</p>
                        <p class="text-xs mt-2">Giro(s):{boleta['GIROS']}</p>
                        <p class="font-bold text-xs mt-2">{boleta['GLOSA']}</p>
                        <p class="text-xs mt-1">{boleta['DOMICILIO_TER']}</p>
                        <p class="text-xs">Teléfono: {boleta['TELEFONO'] or '00-'}</p>
                    </div>
                    <div class="text-center w-1/2 pl-4">
                        <div class="border border-gray-400 p-2 text-sm font-bold leading-none">
                            <p>BOLETA DE PRESTACION DE</p>
                            <p>SERVICIOS DE TERCEROS</p>
                            <p>ELECTRONICA</p>
                        </div>
                        <p class="text-xs font-bold mt-1">N°{boleta['NUMBOL']}</p>
                    </div>
                </div>
                <div class="flex justify-between items-start mb-6">
                    <div class="w-2/3">
                        <p class="text-xs">
                            <span class="font-bold">Señores:</span> {boleta['NOMBRE_TERC']}
                        </p>
                        <p class="text-xs mt-1">
                            <span class="font-bold">Domicilio:</span> {boleta['DOMICILIO_TER']}, {boleta['DESC_COMUNA']}
                        </p>
                    </div>
                    <div class="w-1/3 text-right">
                        <p class="text-xs"><span class="font-bold">Fecha:</span> {boleta['DIA']} de {boleta['MES']} del {boleta['ANO']}</p>
                        <p class="text-xs"><span class="font-bold">Rut:</span> {rut_completo}</p>
                    </div>
                </div>
                <p class="text-xs mb-4">
                    <span class="font-bold">Por atención profesional:</span>
                </p>
                <table class="w-full text-sm border-collapse">
                    <thead>
                        <tr class="border border-gray-400 text-center bg-gray-100">
                            <th class="w-2/3 p-2 border-r border-gray-400">Prestación</th>
                            <th class="w-1/3 p-2">Valor</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="border-b border-l border-r border-gray-400">
                            <td class="p-2 border-r border-gray-400">{boleta['PRESTA1']}</td>
                            <td class="p-2 text-right">{format_number(boleta['VALOR1'])}</td>
                        </tr>
                    </tbody>
                </table>
                <div class="w-full mt-4 flex justify-end">
                    <div class="w-1/2">
                        <div class="flex justify-between items-center text-sm py-1 border-b border-gray-400">
                            <p class="font-bold">Total Honorarios:</p>
                            <p class="font-bold px-2 py-1">{format_number(boleta['BRT'])}</p>
                        </div>
                        <div class="flex justify-between items-center text-sm py-1 border-b border-gray-400">
                            <p>{boleta['TASA_IMP']}% Impuesto Retenido:</p>
                            <p class="px-2 py-1">{format_number(boleta['IMP'])}</p>
                        </div>
                        <div class="flex justify-between items-center text-sm py-1">
                            <p class="font-bold">Total:</p>
                            <p class="font-bold px-2 py-1">{format_number(boleta['NET'])}</p>
                        </div>
                    </div>
                </div>
                <div class="text-center mt-8">
                    <p class="text-xs">Fecha / Hora Emisión: {boleta['DIA']}/{boleta['MES']}/{boleta['ANO']} 23:12</p>
                    <div class="barcode text-6xl mt-2 leading-none">
                        <span class="text-black inline-block">{codigo_barras}</span>
                    </div>
                    <p class="text-xs mt-2">{codigo_barras}</p>
                    <p class="text-xs mt-2">Res. Ex. N°112 de 22/12/2004</p>
                    <p class="text-xs mt-2">Verifique este documento en www.sii.cl</p>
                </div>
            </div>
        </body>
        </html>
        """
        
        # Definir el nombre del archivo de salida
        output_filename = f"boleta_{boleta['NUMBOL']}.pdf"
        output_filepath = os.path.join(output_dir, output_filename)
        
        # Convertir la plantilla HTML a PDF y guardarla
        HTML(string=html_template).write_pdf(output_filepath)
            
        print(f"Boleta N°{boleta['NUMBOL']} generada en '{output_filepath}'")

# Ejemplo de uso de la función
if __name__ == "__main__":
    nombre_archivo_csv = 'Libro1 - prueba 1 boleta.csv'
    generar_boletas_desde_csv(nombre_archivo_csv)
