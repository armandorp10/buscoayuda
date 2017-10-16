from __future__ import absolute_import

import os
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class FunctionalTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            executable_path=r'C:\Users\asus\Downloads\Temp Code\buscoayuda\chromedriver.exe')
        # self.browser.set_window_size(1024, 768)
        # self.browser.implicitly_wait(5000)

    def tearDown(self):
        self.browser.quit()

    def test_1_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)

    def test_2_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()
        self.browser.implicitly_wait(1)

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath(
            "//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        img = os.path.join(os.path.abspath('persona.jpg'))

        if os.name == 'nt':
            img = img.replace("\\", "/")
            imagen.send_keys(img)
        else:
            imagen.send_keys(img)

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()

        self.browser.implicitly_wait(5)
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)

    def test_3_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()
        self.browser.implicitly_wait(3)
        h2 = self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)

    def test_4_login(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_username')
        nombre.send_keys('usuario1')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('usuario1')

        btn = self.browser.find_element_by_id('btn_login')
        btn.click()
        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, '//span[text()="a"]')

        self.assertIn('Nombre1', span.text)

    def test_5_editar(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_username')
        nombre.send_keys('usuario1')

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('usuario1')

        btn = self.browser.find_element_by_id('btn_login')
        btn.click()
        self.browser.implicitly_wait(3)

        btn2 = self.browser.find_element_by_id('btn_edit')
        btn2.click()

        nombreNuevo = self.browser.find_element_by_id('id_firstName')
        nombreNuevo.send_keys('nuevoNombre')

        btn3 = self.browser.find_element_by_id('id_editar')
        btn3.click()

        self.browser.implicitly_wait(3)
        span = self.browser.find_element(By.XPATH, 'id_firstName')

        self.assertIn('nuevoNombre', span.text)

    def test_6_comentario(self):
        self.browser.get('http://localhost:8000')
        span = self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()
        nombre = self.browser.find_element_by_id('id_username')
        nombre.send_keys('usuario1')
        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('usuario1')
        btn = self.browser.find_element_by_id('btn_login')
        btn.click()
        self.browser.implicitly_wait(3)
        comment = self.browser.find_element(By.XPATH, '//textarea[placeholder()="Agreagar comentario"]')
        comment.send_keys('nuevo comentario')
        mail = self.browser.find_element_by_id('correo')
        mail.send_keys('correo@correo.com')
        btn2 = self.browser.find_element(By.XPATH, '//button[title()="Adicionar comentario"]')
        btn2.click()
        self.browser.implicitly_wait(3)
        div = self.browser.find_element_by_id('comentarios')
        self.assertIn('nuevoNombre', div.text)
