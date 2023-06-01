
from fastapi import APIRouter
from config.db import conn
from models.cats import baseCat
from schemas.newCatInsert import newCatInsert
from sqlalchemy import select, insert, update, delete
import json

cats = APIRouter()

@cats.get("/cats/getAllCats")
async def getAllCats():
    try:
        resultJson = {}
        with conn as conected:
            data = conected.execute(baseCat.select()).fetchall()
            for result in data:
                resultJson["id"] = result[0]
                resultJson["catName"] = result[1]
                resultJson["catRace"] = result[2]
                resultJson["catYear"] = result[3]
                resultJson["catImg"] = result[4]
                
        if len(resultJson) > 0: #revisar y corregir tomar todos los datos
            return {"status": 200, "content": resultJson}
        else:
            return {"status": 400, "content": "Error al Obtener Datos"}

    except Exception as error:
        print(error.args)
        print(error)
        print(type(error))
    finally:
        print('Data Obtenida con Exito')

@cats.post("/cats/insertNewCat")
def insertNewCat(newCat: newCatInsert):
    try:
        newCatBody = {"catName": newCat.catName,
                        "catRace": newCat.catRace, 
                        "catYear": newCat.catYear, 
                        "catImg":  newCat.catImg}
        
        with conn as conected:
            conected.execute(insert(baseCat).values(newCatBody))

            return {"status": 200, "content": "Gatito Ingresado con Exito"}
    except Exception as error:
         print(error.args)
         print(error)
         print(type(error))
    finally:
        print('Datos Insertados con Exito')

@cats.get("/cats/getCatId")
def getCatId(id):
    try:
        resultJson = {}
        with conn as conected:
            data = conected.execute(select(baseCat.c["id","catName","catRace","catYear","catImg"]).where(baseCat.c.id == id)).first()
            resultJson["id"] =      data[0]
            resultJson["catName"] = data[1]
            resultJson["catRace"] = data[2]
            resultJson["catYear"] = data[3]
            resultJson["catImg"] =  data[4]
        
        print(resultJson)
        if len(resultJson) > 0:
            return resultJson
        else:
            return {"status": 400, "content": "Error al Obtener Datos"}
    except Exception as error:
       print(error.args)
       print(error)
       print(type(error))
    finally:
        print('Datos Obtenidos Existosamente')


@cats.put("/cats/updateCat")
def updateCat(updateCat: newCatInsert):
    try:
        newCatBody = {"catName": updateCat.catName,
                        "catRace": updateCat.catRace, 
                        "catYear": updateCat.catYear, 
                        "catImg":  updateCat.catImg}
        
        with conn as conected:
            conected.execute(update(baseCat).where(baseCat.c.id == updateCat.id).values(newCatBody))

        return {"status": 200, "content": "Gatito Actualizado con Exito"}
    except Exception as error:
       print(error.args)
       print(error)
       print(type(error))
    finally:
        print('Datos Actualizados Existosamente')

@cats.delete("/cats/deleteCat")
def deleteCat(id):
    try:
        with conn as conected:
            conected.execute(delete(baseCat).where(baseCat.c.id == id))
    
        return {"status": 200, "content": "Gatito Borrado con Exito"}
    except Exception as error:
       print(error.args)
       print(error)
       print(type(error))
    finally:
        print('Gatito Borrado Con Exito')