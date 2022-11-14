# Challenge
## Enunciado del Desafío (DataOps / Ingestando datos)
Un poco de contexto: Los pronósticos respecto al futuro del IoT, hablan de decenas de miles de millones de dispositivos conectados. Entre el 2020 al 2030 se triplicarán la cantidad de los mismos, llegando a superar los 25.000 millones. Las redes de comunicación, en continua evolución,  están ampliando sus capacidades para poder soportar tal cantidad de dispositivos conectados, de cosas conectadas, tanto en zonas urbanas como en zonas remotas, donde la cobertura celular no llega y los dispositivos se conectan mediante redes de comunicación satelital, diseñadas específicamente para IoT, y en donde los datos traficados deben ser optimizados a nivel de bit (zero overhead) si se pretende implementar de manera exitosa, un proyecto IoT que permita optimizar la operación de una industria en particular.

El desafío aquí presentado está enmarcado en este contexto, es decir, optimización de tramas de datos a ser enviados desde y hacia dispositivos remotos de manera tal que sean lo más reducidas en longitud posibles (ahorro de bytes / zero overhead). 
Para esto se solicita desarrollar una librería en Node.js que cuente con al menos dos métodos, encode y decode, que permitan codificar/decodificar o serializar/deserializar un objeto o estructura de datos en función de un formato definido: 
ObjetoDatos <- Formato -> Trama binaria

ObjetoDatos -> Es el objeto que contiene los campos de datos que deben ser codificado/decodificado. Dichos campos pueden de los tipos que se muestran a continuación:

    Tipos requeridos:
•	uint -> entero sin signo, longitud variable (1 a 32bits)
•	int -> entero con signo, longitud variable (complemento a 2, 2 a 32bits)
•	float -> punto flotante de precisión simple (IEEE 754, 32bits)

    Tipos opcionales (valorado):
•	ascii -> ASCII string terminada en #0 | 7bits x caracter


Trama binaria -> Es un Node.js Buffer que contiene los datos codificados de manera tal de optimizar la cantidad de bytes utilizados. 



Formato -> Es un array o vector de objetos, donde cada elemento corresponde a la definición de cada campo del objeto (ObjetoDatos) que se pretende codificar/decodificar. 

    Formato del Vector de objetos [ { tag: "?", type: "?", len: ? } ] donde:
•	tag -> Nombre del campo en el objeto para de/serializar
•	type -> Tipo de dato del campo
•	len -> Longitud en bits del campo (si aplica al tipo)

  
## Esqueleto de la clase (a modo orientativo, no hace falta POO):   
1.	   /** ToDo */
2.	    class BinaryParser {
3.	        /**
4.	        * ToDo
5.	        * v0.1.0 | [autor] | Primera versión
6.	        * 
7.	        * @param {buffer} buffer -> Trama a deserializar
8.	        * @param {*} format -> Formato de serialización (ver notas adjuntas)
9.	        * @return {*} Objeto "composición" (trama deserializada en campos tag = valor)
10.	        * @memberof BinaryParser
11.	        * @version ?
12.	        */
13.	        decode(buffer, format) {
14.	            let _object = {}
15.	            // ToDo
16.	            return _object
17.	        }
18.	 
19.	        /**
20.	        * ?
21.	        * v0.1.0 | [autor] | Primera versión
22.	        * 
23.	        * @param {*} _object -> Objeto a frasear (serializar)
24.	        * @param {*} format -> Formato de serialización (ver notas adjuntas)
25.	        * @return {*} size -> tamaño en bits de la trama. buffer -> Node.js Buffer.
26.	        * @memberof BinaryParser
27.	        * @version ?
28.	        */
29.	        encode(_object, format) {
30.	            const buffer = Buffer.alloc(?);
31.	            // ToDo
32.	            return { size, buffer };
33.	        }
34.	    } 

## Ejemplo
1.		const format1 = [
2.			{ tag: "PTemp", type: "int", len: 12 },
3.			{ tag: "BattVolt.value", type: "int", len: 12 },
4.			{ tag: "WaterLevel", type: "int", len: 8 },
5.		]; 
6.			
7.		var data = { PTemp: 268, BattVolt.value: 224, WaterLevel: 115 }; 
8.	 
9.		var bp = new BinaryParser();
10.		var dataEncoded = bp.encode(data, format1); 
11.		console.log(dataEncoded.buffer.toString('hex')); //prints 10C0E073
12.	  console.log(dataEncoded.size); //prints 32
13.	  var dataDecoded = bp.decode(dataEncoded.buffer, format1);
14.		console.log(dataDecoded) //prints { PTemp: 268, ‘BattVolt.value’: 224, WaterLevel: 115 }
15.	 

## Otros ejemplos de Formatos
1.	    const format2 = [
2.	        { tag: "var0.value", type: "uint", len: 2 },
3.	        { tag: "var1.value", type: "uint", len: 2 },
4.	        { tag: "var2.value", type: "uint", len: 7 },
5.	        { tag: "var3.value", type: "uint", len: 11 },
6.	        { tag: "var4.value", type: "int", len: 10 },
7.	        { tag: "var5.value", type: "uint", len: 16 },
8.	        { tag: "var6.value", type: "float" },
9.	        { tag: "var7.value", type: "uint", len: 16 },
10.	        { tag: "var8.value", type: "uint", len: 32 },
11.	        { tag: "var9.value", type: "uint", len: 8 },
12.	    ]; 
1.	    const format3 = [
2.	        { tag: "var0.Temp_C_2_Avg", type: "float" },
3.	        { tag: "var0.DOppm", type: "float" },
4.	        { tag: "var0.TurbNTU", type: "float" },
5.	        { tag: "var0.Lvl_corr_Avg", type: "float" },
6.	        { tag: "var0.Cond_Avg", type: "float" },
7.	        { tag: "var0.pH_Avg", type: "float" },
8.	        { tag: "var0.TimeStamp", type: "float" },
9.	        { tag: "var0.BattV_Avg", type: "float" },
10.	        { tag: "var0.BattV_Min", type: "float" },
11.	        { tag: "var1.Temp_C_2_Avg", type: "float" },
12.	        { tag: "var1.DOppm", type: "float" },
13.	        { tag: "var1.TurbNTU", type: "float" },
14.	        { tag: "var1.Lvl_corr_Avg", type: "float" },
15.	        { tag: "var1.Cond_Avg", type: "float" },
16.	        { tag: "var1.pH_Avg", type: "float" },
17.	        { tag: "var1.TimeStamp", type: "float" },
18.	        { tag: "var1.BattV_Avg", type: "float" },
19.	        { tag: "var1.BattV_Min", type: "float" },
20.	    ]; 
    
## Otro Ejemplo de deserialización

    La trama de datos -> 0x010203
    
    Con el formato -> [
        { tag: "v0", type: "int", len: 8 },
        { tag: "v1", type: "int", len: 8 },
        { tag: "v2", type: "int", len: 8 },
    ]    
    
    Produce un objeto -> {
        v0: 1,
        v1: 2,
        v2: 3
    }

## Para tener en cuenta

A elección, y según preferencias, puedes utilizar:

•	Typescript
•	POO o Funcional
•	Librerías de terceros 

Se valora:

•	Código estructurado y documentado (JSDoc)
•	Testeo unitario (Jest)
•	Resultados en repositiorio Git
•	Poder configurar bit / byte / word order.
•	Tipo ASCII string
•	Manejo de errores / excepciones


