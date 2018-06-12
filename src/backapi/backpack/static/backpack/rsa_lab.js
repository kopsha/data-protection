function encrypt(publicPem, message)
{
	var publicKey = forge.pki.publicKeyFromPem(publicPem);

	var encrypted = publicKey.encrypt(message, "RSA-OAEP", {
				md: forge.md.sha256.create(),
				mgf1: forge.mgf1.create()
			});

	return forge.util.encode64(encrypted);
}

function decrypt(privatePem, message)
{
	var privKey = forge.pki.privateKeyFromPem(privatePem);

	var decryptMsg = privKey.decrypt(forge.util.decode64(message), "RSA-OAEP", {
				md: forge.md.sha256.create(),
				mgf1: forge.mgf1.create()
			});

	return decryptMsg;
}
