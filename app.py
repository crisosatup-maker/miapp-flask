from flask import Flask, render_template, request, make_response

import os

app = Flask(__name__)

 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contactate')
def contactate():
    
 return render_template('contactate.html')


@app.route('/nosotros')
def nosotros():
    
 return render_template('nosotros.html')

@app.route('/sale')
def sale():
     productos_sale = [
        {"nombre": "Remera básica", "imagen": "img/remera.jpg", "precio": "$2,000"},
        {"nombre": "Pantalón jogger", "imagen": "img/jogger.jpg", "precio": "$4,000"}
    ]
     return render_template('Sale.html', productos=productos_sale)


@app.route('/medias')
def medias():
    modelos_medias = [
        {            
            "nombretitulo":"Medias Media Caña ",
            "descripcion":"Abarcan del 34 al 44",
            "talles":"",
            "productos":[
                {"nombre": "Adidas blanco y negro", "imagen": "imagenes/madidas1.jpg", "precio": "$2800"},
                {"nombre": "Adidas negras lisa", "imagen": "imagenes/madidas2.jpg", "precio": "$2800"},
                {"nombre": "Adidas blancas con lineas azul, celeste y negra", "imagen": "imagenes/madidas3.jpg", "precio": "$2800"},
                {"nombre": "Adidas blancas con amarillo", "imagen": "imagenes/madidas4.jpg", "precio": "$2800"},
                {"nombre": "Adidas blancas con lineas naranja, rosa y verde", "imagen": "imagenes/madidas5.jpg", "precio": "$2800"},
                {"nombre": "Adidas negras con rojo y blanco", "imagen": "imagenes/madidas6.jpg", "precio": "$2800"},
                {"nombre": "Adidas grises con lineas blancas", "imagen": "imagenes/madidas8.jpg", "precio": "$2800"},
                {"nombre": "Adidas negras con lineas rojas", "imagen": "imagenes/madidas9.jpg", "precio": "$2800"},
                {"nombre": "Adidas celestes con lineas blancas", "imagen": "imagenes/madidas10.jpg", "precio": "$2800"},
                {"nombre": "Adidas negras con lineas amarillas", "imagen": "imagenes/madidas11.jpg", "precio": "$2800"},
                {"nombre": "Adidas rosas", "imagen": "imagenes/madidas12.jpg", "precio": "$2800"},
                {"nombre": "Adidas blancas con lineas rosas", "imagen": "imagenes/madidas13.jpg", "precio": "$2800"},
                {"nombre": "Adidas blancas con lineas mostaza", "imagen": "imagenes/madidas14.jpg", "precio": "$2800"},
                {"nombre": "Adidas rosas con lineas fuccia", "imagen": "imagenes/madidas15.jpg", "precio": "$2800"},
                {"nombre": "Adidas blancas con lineas mostaza, rojo y rosa", "imagen": "imagenes/madidas16.jpg", "precio": "$2800"},
                {"nombre": "Adidas negras con amarillo y morado", "imagen": "imagenes/madidas17.jpg", "precio": "$2800"},
                {"nombre": "Nike blancas corazones", "imagen": "imagenes/mnike15.jpg", "precio": "$2800"},
                {"nombre": "Nike blancas paltas", "imagen": "imagenes/mnike16.jpg", "precio": "$2800"},
                {"nombre": "Nike blancas capybaras", "imagen": "imagenes/mnike17.jpg", "precio": "$2800"},
                {"nombre": "Nike blancas con azul y rosa", "imagen": "imagenes/mnike1.jpg", "precio": "$2800"},
                {"nombre": "Nike turquesas", "imagen": "imagenes/mnike2.jpg", "precio": "$2800"},
                {"nombre": "Nike blancas y negras", "imagen": "imagenes/mnike3.jpg", "precio": "$2800"},
                {"nombre": "Nike naranjas", "imagen": "imagenes/mnike4.jpg", "precio": "$2800"},
                {"nombre": "Nike lilas", "imagen": "imagenes/mnike5.jpg", "precio": "$2800"},
                {"nombre": "Nike blancas", "imagen": "imagenes/mnike6.jpg", "precio": "$2800"},
                {"nombre": "Nike marrones", "imagen": "imagenes/mnike7.jpg", "precio": "$2800"},
                {"nombre": "Nike negras con letras", "imagen": "imagenes/mnike8.jpg", "precio": "$2800"},
                {"nombre": "Nike rosa con manchitas blancas", "imagen": "imagenes/mnike9.jpg", "precio": "$2800"},
                {"nombre": "Nike negras con manchitas blancas", "imagen": "imagenes/mnike10.jpg", "precio": "$2800"},
                {"nombre": "Nike blancas con colores", "imagen": "imagenes/mnike11.jpg", "precio": "$2800"},
                {"nombre": "Nike grises", "imagen": "imagenes/mnike12.jpg", "precio": "$2800"},
                {"nombre": "Nike blancas con manchitas negras", "imagen": "imagenes/mnike13.jpg", "precio": "$2800"},
                {"nombre": "Nike blancas con letras", "imagen": "imagenes/mnike14.jpg", "precio": "$2800"},
                {"nombre": "Fila blancas con lineas rojas y azul", "imagen": "imagenes/mfila.jpg", "precio": "$2800"},
                {"nombre": "Jordan blancas con negro", "imagen": "imagenes/mjordan.jpg", "precio": "$2800"},
                {"nombre": "Blancas con lineas negras", "imagen": "imagenes/mlineas1.jpg", "precio": "$2800"},
                {"nombre": "Blancas con lineas azules", "imagen": "imagenes/mlineas2.jpg", "precio": "$2800"},
                {"nombre": "Vans negras", "imagen": "imagenes/mvans.jpg", "precio": "$2800"}
            ]
        },
        {            
            "nombretitulo":"Soquetes Animados ",
            "descripcion":"Abarcan del 34 al 44",
            "talles":"",
            "productos":[
                {"nombre": "Soquete Capybara", "imagen": "imagenes/msoquetecapybara.png", "precio": "$1600"},
                {"nombre": "Soquete Carlitos", "imagen": "imagenes/msoquetecarlitos.png", "precio": "$1600"},
                {"nombre": "Soquete Hermione - Harry Potter", "imagen": "imagenes/msoquetehermione.png", "precio": "$1600"},
                {"nombre": "Soquete Harry Potter", "imagen": "imagenes/msoqueteharrypotter1.png", "precio": "$1600"},
                {"nombre": "Soquete Boca Junior", "imagen": "imagenes/msoqueteboca.png", "precio": "$1600"},
                {"nombre": "Soquete River Plate", "imagen": "imagenes/msoqueteriver.png", "precio": "$1600"},
                {"nombre": "Soquete Lilo y Stitch, rosa y celeste ", "imagen": "imagenes/msoquetestitch1.png", "precio": "$1600"},
                {"nombre": "Soquete Lilo y Stitch, rosa ", "imagen": "imagenes/msoquetestitch2.png", "precio": "$1600"},
                {"nombre": "Soquete Lillo y Stitch, azul ", "imagen": "imagenes/msoquetestitch3.png", "precio": "$1600"},
                {"nombre": "Soquete Mickey Mouse - Disney", "imagen": "imagenes/msoquetemickey1.png", "precio": "$1600"},
                {"nombre": "Soquete Mickey Mouse blanco y negro", "imagen": "imagenes/msoquetemickey2.png", "precio": "$1600"},
                {"nombre": "Soquete Cerdito", "imagen": "imagenes/msoquetechanchito.png", "precio": "$1600"},
                {"nombre": "Soquete Jerry", "imagen": "imagenes/msoquetejerry.png", "precio": "$1600"},
                {"nombre": "Soquete Tom", "imagen": "imagenes/msoquetetom.png", "precio": "$1600"},
                {"nombre": "Soquete Mafalda", "imagen": "imagenes/msoquetemafalda.png", "precio": "$1600"},
                {"nombre": "Soquete Pato Lucas", "imagen": "imagenes/msoquetepatolucas.png", "precio": "$1600"},
                {"nombre": "Soquete Kuromi", "imagen": "imagenes/msoquetekuromi.png", "precio": "$1600"},
                {"nombre": "Soquete Snoopy", "imagen": "imagenes/msoquetesnoppy.png", "precio": "$1600"},
                {"nombre": "Soquete Escandalosos", "imagen": "imagenes/msoqueteescandalosos.png", "precio": "$1600"},
                {"nombre": "Soquete Garfield", "imagen": "imagenes/msoquetegarfield.png", "precio": "$1600"},
                {"nombre": "Soquete Sonic", "imagen": "imagenes/msoquetesonic.png", "precio": "$1600"},
                {"nombre": "Soquete Chicas Superpoderosas", "imagen": "imagenes/msoquetesuperpoderosas.png", "precio": "$1600"}
                
            ]
        }
    ]
    return render_template('medias.html', modelos=modelos_medias)

@app.route('/pijamas')
def pijamas():
    modelos_pijamas = [
        {
            "nombretitulo":"Conjunto de TOP + SHORT ",
            "descripcion":"Tela modal con lycra, elastizada y fresca.El top tiene elástico.",
            "talles":"Talle único.Medidas -> ||TOP: sisa a sisa 42cm, largo 35cm.Abarca busto hasta talle 100.||SHORT: cintura sin estirar 29cm, estirada 50cm, cadera 48cm, largo 30cm. Abarca hasta un talle 44 de pantalón||",
            "productos":[
                {"nombre": "Conjunto Garfield", "imagen": "imagenes/ptopgarfield.jpg", "precio": "$14200","Talle":"único (medidas en descripción)"},
                {"nombre": "Conjunto Harry Potter", "imagen": "imagenes/ptopharrypotter.jpg", "precio": "$14200","Talle":"único (medidas en descripción)"},
                {"nombre": "Conjunto Mafalda", "imagen": "imagenes/ptopmafalda.jpg", "precio": "$14200","Talle":"único (medidas en descripción)"},
                {"nombre": "Conjunto Mickey Mouse", "imagen": "imagenes/ptopmickey1.jpg", "precio": "$14200","Talle":"único (medidas en descripción)"},
                {"nombre": "Conjunto Mickey Mouse", "imagen": "imagenes/ptopmickey2.jpg", "precio": "$14200","Talle":"único (medidas en descripción)"},
                {"nombre": "Conjunto Mariposas", "imagen": "imagenes/ptopmariposa.jpg", "precio": "$14200","Talle":"único (medidas en descripción)"},
                {"nombre": "Conjunto Lilo y Stitch", "imagen": "imagenes/ptoplilo1.jpg", "precio": "$14200","Talle":"único (medidas en descripción)"},
                {"nombre": "Conjunto Lilo y Stitch", "imagen": "imagenes/ptoplilo2.jpg", "precio": "$14200","Talle":"único (medidas en descripción)"},
                {"nombre": "Conjunto Kuromi", "imagen": "imagenes/ptopkuromi.jpg", "precio": "$14200","Talle":"único (medidas en descripción)"},
                {"nombre": "Conjunto Snoopy", "imagen": "imagenes/ptopsnoopy.jpg", "precio": "$14200","Talle":"único (medidas en descripción)"},
                {"nombre": "Conjunto Tom y Jerry", "imagen": "imagenes/ptoptomyjerry.jpg", "precio": "$14200","Talle":"único (medidas en descripción)"}
            ]
        },

        {
            "nombretitulo":"CAMISEROS",
            "descripcion":"Camisero confeccionado en modal soft de alta calidad, un tejido suave, liviano y delicado al tacto, ideal para brindar confort y frescura durante todo el día.\nDiseñado con cuello clásico y cierre de botones frontales.",
            "talles":"Talle 2 (38/40) - Talle 3  (42/44) - Talle 4 (46/48) - Talle 5 (50/52)",
            "productos":[
                {"nombre": "Camisero Espacio", "imagen": "imagenes/pcamiseroespacio2.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Espacio", "imagen": "imagenes/pcamiseroespacio1.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Hello Kitty", "imagen": "imagenes/pcamiserokitty1.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Hello Kitty", "imagen": "imagenes/pcamiserokitty2.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Animal Print", "imagen": "imagenes/pcamiseroanimalprint1.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Animal Print", "imagen": "imagenes/pcamiseroanimalprint2.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Mickey Mouse", "imagen": "imagenes/pcamiseromickey1.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Mickey Mouse", "imagen": "imagenes/pcamiseromickey2.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Lilo y Stitch", "imagen": "imagenes/pcamiserolilo1.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Lilo y Stitch", "imagen": "imagenes/pcamiserolilo2.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Lilo y Stitch", "imagen": "imagenes/pcamiserolilo3.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Lilo y Stitch", "imagen": "imagenes/pcamiserolilo4.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Lilo y Stitch", "imagen": "imagenes/pcamiserolilo5.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Palta", "imagen": "imagenes/pcamiseropalta.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Palmeras", "imagen": "imagenes/pcamiseropalmera.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Corazones", "imagen": "imagenes/pcamiserocorazon1.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Corazones", "imagen": "imagenes/pcamiserocorazon2.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Corazones", "imagen": "imagenes/pcamiserocorazon3.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Luna Sailon Moon", "imagen": "imagenes/pcamiseroSailorMoon.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"},
                {"nombre": "Camisero Los Aristogatos", "imagen": "imagenes/pcamiseroarisogatos.jpg", "precio": "$27000","Talles":"2 (38/40) - 3 (42/44) - 4 (46/48) - 5 (50/52)"}
                          
                
                 
            ]
        },
        
        {
            "nombretitulo":"Pijama MANGA CORTA + SHORT",
            "descripcion":"Pijama de modal con lycra premium.Pantalón elastizado en la cintura.\n Remera y pantalón corte unisex (para hombre y mujer).",
            "talles":"Talles reales del 1 al 7",
            "productos":[
                {"nombre": "Pijama Hello Kitty", "imagen": "imagenes/pcortokitty.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Charlie Brown y Snoopy ", "imagen": "imagenes/pcortocharlie.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Garfield", "imagen": "imagenes/pcortogarfield.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Lotso", "imagen": "imagenes/pcortolotso.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Minnie Mouse", "imagen": "imagenes/pcortominnie.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Lilo y Stitch", "imagen": "imagenes/pcortostitch1.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Lilo y Stitch", "imagen": "imagenes/pcortostitch2.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Lilo y Stitch", "imagen": "imagenes/pcortostitch3.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Lilo y Stitch", "imagen": "imagenes/pcortostitch4.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Mafalda", "imagen": "imagenes/pcortomafalda.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Vaquita", "imagen": "imagenes/pcortovaca.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Boca Junior", "imagen": "imagenes/pcortoboca.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama River Plate", "imagen": "imagenes/pcortoriver.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Melón", "imagen": "imagenes/pcortofruta.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Los Aristogatos", "imagen": "imagenes/pcortogato.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Osito", "imagen": "imagenes/pcortooso.jpg", "precio": "$17500","Talle":"del 1 al 7"},
                {"nombre": "Pijama Betty Boop", "imagen": "imagenes/pcortobetty.jpg", "precio": "$17500","Talle":"del 1 al 7"}            
                
                 
            ]
        },

        {
            "nombretitulo":"Pijama MANGA CORTA + PANTALÓN LARGO",
            "descripcion":"Pijama de modal con lycra premium.Pantalón elastizado en la cintura y en el largo de las piernas, con bolsillos.\n Remera y pantalón corte unisex (para hombre y mujer).",
            "talles":"Talles reales del 38 al 52",
            "productos":[
                {"nombre": "Pijama Mickey", "imagen": "imagenes/pmickey1.jpg", "precio": "$25000"},
                {"nombre": "Pijama Mickey", "imagen": "imagenes/pmickey2.jpg", "precio": "$25000"},
                {"nombre": "Pijama Mickey", "imagen": "imagenes/pmickey3.jpg", "precio": "$25000"},
                {"nombre": "Pijama Hello Kitty", "imagen": "imagenes/pkitty1.jpg", "precio": "$25000"},
                {"nombre": "Pijama Hello Kitty", "imagen": "imagenes/pkitty2.jpg", "precio": "$25000"},
                {"nombre": "Pijama Harry Potter", "imagen": "imagenes/pharrypotter.jpg", "precio": "$25000"},
                {"nombre": "Pijama Lilo y Stitch", "imagen": "imagenes/pstitch1.jpg", "precio": "$25000"},
                {"nombre": "Pijama Lilo y Stitch", "imagen": "imagenes/pstitch2.jpg", "precio": "$25000"},
                {"nombre": "Pijama Paltas", "imagen": "imagenes/ppalta.jpg", "precio": "$25000"},
                {"nombre": "Pijama Pato Lucas", "imagen": "imagenes/ppato.jpg", "precio": "$25000"}
            ]
        }

        
    ]
    return render_template('pijamas.html', modelos=modelos_pijamas)

@app.route('/novedades')
def novedades():
    modelos_novedades = [
        {
            "nombretitulo":"Conjunto deportivo",
            "descripcion":"Remeron + Biker + Medias media caña.",
            "talles":"-",
            "productos":[
                {"nombre": "Conjunto deportivo Chicas Superopoderosas (remerón blanco) ", "imagen": "imgnovedades/depo3blanco.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Chicas Superopoderosas (remerón negro) ", "imagen": "imgnovedades/depo3negro.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Burbuja (remerón celeste) ", "imagen": "imgnovedades/depoburbujaceleste.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Bombón (remerón verde) ", "imagen": "imgnovedades/depobombonverde.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Bombón (remerón negro) ", "imagen": "imgnovedades/depobombonnegro.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Bombón (remerón rojo) ", "imagen": "imgnovedades/depobombonrojo.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Bombón (remerón verde agua) ", "imagen": "imgnovedades/depobombonverdeagua.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Bellota (remerón negro) ", "imagen": "imgnovedades/depobellotanegro.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Bellota (remerón fuccia) ", "imagen": "imgnovedades/depobellotafuccia.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Bellota (remerón beige) ", "imagen": "imgnovedades/depobellotamarron1.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Bellota (remerón verde) ", "imagen": "imgnovedades/depobellotaverde.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Bellota (remerón marrón) ", "imagen": "imgnovedades/depobellotamarron2.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Lola Bunny (remerón fuccia) ", "imagen": "imgnovedades/depoconejafuccia.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Lola Bunny (remerón celeste) ", "imagen": "imgnovedades/depoconejaceleste.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Pocahontas (remerón verde militar) ", "imagen": "imgnovedades/depopocahontasverde.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Betty Boop (remerón negro) ", "imagen": "imgnovedades/depobettynegro.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Tinkerbell (remerón rojo) ", "imagen": "imgnovedades/depotinkerbellrojo.PNG", "precio": "$14200"},
                {"nombre": "Conjunto deportivo Hello Kitty (remerón fuccia) ", "imagen": "imgnovedades/depokittyfuccia.PNG", "precio": "$14200"}
            ]
        }
    ]
    return render_template('novedades.html', modelos=modelos_novedades)


@app.route('/verano')
def verano():
    modelos_verano= [
        {
            "nombretitulo":"Batas de baño",
            "descripcion":"Bata de microtoalla, excelente calidad",
            "talles":"Talle único, abarca hasta un talle 6 de adulto..Medidas de frente-> ||hombro a hombro: 61cm.||Sisa a sisa: 68cm.||Largo: 98cm.",
            "productos":[
     
                {"nombre": "Bata Corazones", "imagen": "imgverano/bcorazon.jpg", "precio": "$2,000"},
                {"nombre": "Bata Paltas", "imagen": "imgverano/bpalta.jpg", "precio": "$4,000"},
                {"nombre": "Bata Stitch", "imagen": "imgverano/bstitch.jpg", "precio": "$2,000"},
                {"nombre": "Bata Harry Potter", "imagen": "imgverano/bharrypotter.jpg", "precio": "$4,000"},
                {"nombre": "Bata Hello Kitty", "imagen": "imgverano/bkitty.jpg", "precio": "$2,000"},
                {"nombre": "Bata Boca Junior", "imagen": "imgverano/bboca.jpg", "precio": "$4,000"},
                {"nombre": "Bata River Plate", "imagen": "imgverano/briver.jpg", "precio": "$2,000"},
                {"nombre": "Bata Luna", "imagen": "imgverano/bluna.jpg", "precio": "$4,000"},
                {"nombre": "Bata Cerezas", "imagen": "imgverano/bcerezas.jpg", "precio": "$2,000"},
                {"nombre": "Bata Candy", "imagen": "imgverano/bdulces.jpg", "precio": "$4,000"},
                {"nombre": "Bata Mickey Mouse", "imagen": "imgverano/bmickey.jpg", "precio": "$4,000"}
            ]
        }
    ]
    return render_template('verano.html', modelos=modelos_verano)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)



