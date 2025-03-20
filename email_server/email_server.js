require('dotenv').config(); // Load environment variables
const express = require('express');
const nodemailer = require('nodemailer');

const app = express();
app.use(express.json()); // To parse JSON bodies

// Configure your SMTP transporter
let transporter = nodemailer.createTransport({
  host: process.env.SMTP_HOST,
  port: parseInt(process.env.SMTP_PORT),
  secure: process.env.SMTP_PORT === '465', // Use secure true if using port 465
  auth: {
    user: process.env.SMTP_USER,
    pass: process.env.SMTP_PASSWORD
  }
});

// POST endpoint to send email
app.post('/send-email', async (req, res) => {
  try {
    // Updated payload now expects additional fields
    // Expected payload: { "orderId": "123", "orderEmail": "cliente@example.com", "status": "APROVADO", "empresa": "Empresa XYZ", "descricao": "Descrição do pedido", "valor": "300.00" }
    const { orderId, orderEmail, status, empresa, descricao, valor } = req.body;

    if (!orderId || !orderEmail || !status || !empresa || !descricao || !valor) {
      return res.status(400).json({ error: 'Faltam campos obrigatórios.' });
    }

    // Construct the HTML email options with inline CSS for a better layout
    let mailOptions = {
      from: '"Serviço de Pedidos" <pugarosabal@gmail.com>', // sender address
      to: orderEmail, // recipient
      subject: `Actualização do Estado do Pedido ${orderId}`, // Subject line in Portuguese
      html: `
        <html>
          <head>
            <meta charset="UTF-8">
            <title>Actualização do Estado do Pedido</title>
          </head>
          <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border: 1px solid #dddddd; border-radius: 5px; padding: 20px;">
              <h2 style="color: #333333;">Actualização do Estado do Pedido</h2>
              <p>Caro Cliente,</p>
              <p>O seu pedido (ID: <strong>${orderId}</strong>) efetuado pela <strong>${empresa}</strong> encontra-se com o estado: <strong>${status}</strong>.</p>
              <p><strong>Detalhes do Pedido:</strong></p>
              <ul>
                <li><strong>Descrição:</strong> ${descricao}</li>
                <li><strong>Valor:</strong> €${valor}</li>
              </ul>
              <p>Obrigado pela sua preferência.</p>
              <p>Com os melhores cumprimentos,<br/>Equipa de Atendimento</p>
            </div>
          </body>
        </html>
      `
    };

    // Send the email
    let info = await transporter.sendMail(mailOptions);
    console.log(`Email enviado: ${info.messageId}`);

    res.status(200).json({ message: 'Email enviado com sucesso.' });
  } catch (error) {
    console.error('Erro ao enviar email:', error);
    res.status(500).json({ error: 'Falha ao enviar email.' });
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor Node a escutar na porta ${PORT}`);
});
