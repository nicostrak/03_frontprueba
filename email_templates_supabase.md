# Plantillas de Correo BoletaPro para Supabase

Copia y pega este código HTML en la sección **Authentication > Email Templates** de tu panel de Supabase.

---

## 1. Confirmación de Registro (Confirm Signup)
**Asunto:** 🎓 Bienvenido a BoletaPro - Confirma tu cuenta

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Confirma tu correo</title>
</head>
<body style="margin: 0; padding: 0; background-color: #121212; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #f5f5f5;">
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #121212; padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="100%" max-width="600" style="max-width: 600px; background-color: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 12px; overflow: hidden;">
                    <!-- Header -->
                    <tr>
                        <td style="padding: 40px 40px 20px 40px; text-align: center;">
                            <h1 style="color: #00B37E; margin: 0; font-size: 28px; font-weight: 800; letter-spacing: -0.5px;">BoletaPro</h1>
                        </td>
                    </tr>
                    <!-- Hero Section -->
                    <tr>
                        <td style="padding: 0 40px 40px 40px; text-align: center;">
                            <h2 style="color: #ffffff; margin: 0 0 16px 0; font-size: 24px;">¡Hola! Confirma tu cuenta</h2>
                            <p style="color: #a0a0a0; font-size: 16px; line-height: 24px; margin: 0;">Gracias por unirte a BoletaPro. Estamos listos para ayudarte a automatizar tus boletas de honorarios. Solo falta confirmar tu acceso.</p>
                        </td>
                    </tr>
                    <!-- CTA Button -->
                    <tr>
                        <td style="padding: 0 40px 40px 40px; text-align: center;">
                            <a href="{{ .ConfirmationURL }}" style="display: inline-block; padding: 16px 36px; background-color: #00B37E; color: #ffffff; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 16px; box-shadow: 0 4px 12px rgba(0, 179, 126, 0.3);">Confirmar Email</a>
                        </td>
                    </tr>
                    <!-- Footer Info -->
                    <tr>
                        <td style="padding: 40px; background-color: #151515; border-top: 1px solid #2a2a2a; text-align: center;">
                            <p style="color: #666666; font-size: 12px; margin: 0 0 10px 0;">Si no creaste esta cuenta, puedes ignorar este mensaje.</p>
                            <p style="color: #666666; font-size: 12px; margin: 0;">&copy; 2025 BoletaPro. Todos los derechos reservados.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 2. Recuperación de Contraseña (Reset Password)
**Asunto:** 🔑 Restablecer tu contraseña en BoletaPro

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Recuperar Contraseña</title>
</head>
<body style="margin: 0; padding: 0; background-color: #121212; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #f5f5f5;">
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #121212; padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="100%" max-width="600" style="max-width: 600px; background-color: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 12px; overflow: hidden;">
                    <!-- Header -->
                    <tr>
                        <td style="padding: 40px 40px 20px 40px; text-align: center;">
                            <h1 style="color: #00B37E; margin: 0; font-size: 28px; font-weight: 800; letter-spacing: -0.5px;">BoletaPro</h1>
                        </td>
                    </tr>
                    <!-- Content -->
                    <tr>
                        <td style="padding: 0 40px 40px 40px; text-align: center;">
                            <h2 style="color: #ffffff; margin: 0 0 16px 0; font-size: 24px;">¿Olvidaste tu contraseña?</h2>
                            <p style="color: #a0a0a0; font-size: 16px; line-height: 24px; margin: 0;">Recibimos una solicitud para restablecer tu contraseña. Haz clic en el botón de abajo para elegir una nueva.</p>
                        </td>
                    </tr>
                    <!-- CTA Button -->
                    <tr>
                        <td style="padding: 0 40px 40px 40px; text-align: center;">
                            <a href="{{ .ConfirmationURL }}" style="display: inline-block; padding: 16px 36px; background-color: #00B37E; color: #ffffff; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 16px; box-shadow: 0 4px 12px rgba(0, 179, 126, 0.3);">Cambiar Contraseña</a>
                        </td>
                    </tr>
                    <!-- Warning -->
                    <tr>
                        <td style="padding: 0 40px 40px 40px; text-align: center;">
                            <p style="color: #cc4444; font-size: 13px; line-height: 20px; font-style: italic;">Por seguridad, este enlace expirará en breve.</p>
                        </td>
                    </tr>
                    <!-- Footer Info -->
                    <tr>
                        <td style="padding: 40px; background-color: #151515; border-top: 1px solid #2a2a2a; text-align: center;">
                            <p style="color: #666666; font-size: 12px; margin: 0 0 10px 0;">Si no solicitaste este cambio, simplemente ignora este correo.</p>
                            <p style="color: #666666; font-size: 12px; margin: 0;">&copy; 2025 BoletaPro. Todos los derechos reservados.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 3. Enlace Mágico / Cambio de Email (Magic Link / Email Change)
**Asunto:** ⚡ Acceso rápido a BoletaPro

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Acceso rápido</title>
</head>
<body style="margin: 0; padding: 0; background-color: #121212; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #f5f5f5;">
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #121212; padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="100%" max-width="600" style="max-width: 600px; background-color: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 12px; overflow: hidden;">
                    <!-- Header -->
                    <tr>
                        <td style="padding: 40px 40px 20px 40px; text-align: center;">
                            <h1 style="color: #00B37E; margin: 0; font-size: 28px; font-weight: 800; letter-spacing: -0.5px;">BoletaPro</h1>
                        </td>
                    </tr>
                    <!-- Content -->
                    <tr>
                        <td style="padding: 0 40px 40px 40px; text-align: center;">
                            <h2 style="color: #ffffff; margin: 0 0 16px 0; font-size: 24px;">Entra sin contraseña</h2>
                            <p style="color: #a0a0a0; font-size: 16px; line-height: 24px; margin: 0;">Usa este enlace seguro para acceder a tu plataforma directamente, sin necesidad de escribir tu clave.</p>
                        </td>
                    </tr>
                    <!-- CTA Button -->
                    <tr>
                        <td style="padding: 0 40px 40px 40px; text-align: center;">
                            <a href="{{ .ConfirmationURL }}" style="display: inline-block; padding: 16px 36px; background-color: #00B37E; color: #ffffff; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 16px; box-shadow: 0 4px 12px rgba(0, 179, 126, 0.3);">Entrar a mi Cuenta</a>
                        </td>
                    </tr>
                    <!-- Footer Info -->
                    <tr>
                        <td style="padding: 40px; background-color: #151515; border-top: 1px solid #2a2a2a; text-align: center;">
                            <p style="color: #666666; font-size: 12px; margin: 0 0 10px 0;">Este enlace solo funciona una vez.</p>
                            <p style="color: #666666; font-size: 12px; margin: 0;">&copy; 2025 BoletaPro. Todos los derechos reservados.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

---

## 4. Notificación de Contraseña Cambiada (Password Changed)
**Asunto:** 🔐 Contraseña actualizada en BoletaPro

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contraseña Cambiada</title>
</head>
<body style="margin: 0; padding: 0; background-color: #121212; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #f5f5f5;">
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="background-color: #121212; padding: 40px 0;">
        <tr>
            <td align="center">
                <table width="100%" max-width="600" style="max-width: 600px; background-color: #1a1a1a; border: 1px solid #2a2a2a; border-radius: 12px; overflow: hidden;">
                    <!-- Header -->
                    <tr>
                        <td style="padding: 40px 40px 20px 40px; text-align: center;">
                            <h1 style="color: #00B37E; margin: 0; font-size: 28px; font-weight: 800; letter-spacing: -0.5px;">BoletaPro</h1>
                        </td>
                    </tr>
                    <!-- Content -->
                    <tr>
                        <td style="padding: 0 40px 40px 40px; text-align: center;">
                            <h2 style="color: #ffffff; margin: 0 0 16px 0; font-size: 24px;">Contraseña Actualizada</h2>
                            <p style="color: #a0a0a0; font-size: 16px; line-height: 24px; margin: 0;">Te informamos que la contraseña de tu cuenta en BoletaPro ha sido cambiada exitosamente.</p>
                        </td>
                    </tr>
                    <!-- Info Box -->
                    <tr>
                        <td style="padding: 0 40px 40px 40px;">
                            <div style="background-color: #121212; border: 1px solid #2a2a2a; border-radius: 8px; padding: 20px; text-align: left;">
                                <p style="color: #e53e3e; font-size: 14px; margin: 0; font-weight: bold;">¿No fuiste tú?</p>
                                <p style="color: #a0a0a0; font-size: 14px; margin: 10px 0 0 0; line-height: 20px;">Si no realizaste este cambio, por favor contacta a nuestro equipo de soporte de inmediato o intenta recuperar tu cuenta usando tu correo electrónico.</p>
                            </div>
                        </td>
                    </tr>
                    <!-- CTA -->
                    <tr>
                        <td style="padding: 0 40px 40px 40px; text-align: center;">
                            <a href="https://tu-usuario.github.io/proyectobht/" style="display: inline-block; padding: 14px 28px; border: 1px solid #00B37E; color: #00B37E; text-decoration: none; border-radius: 8px; font-weight: bold; font-size: 14px;">Ir al Panel</a>
                        </td>
                    </tr>
                    <!-- Footer Info -->
                    <tr>
                        <td style="padding: 40px; background-color: #151515; border-top: 1px solid #2a2a2a; text-align: center;">
                            <p style="color: #666666; font-size: 12px; margin: 0;">&copy; 2025 BoletaPro. Todos los derechos reservados.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```
