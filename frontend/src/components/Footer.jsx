import { FaFacebook, FaTwitter, FaInstagram } from 'react-icons/fa';

export default function Footer() {
  return (
    <footer className="bg-green-600 text-white py-2 px-6 bottom-0 w-full fixed z-50" >
      <div className="max-w-7xl mx-auto text-center">
        <div className="mt-2 flex justify-center">
          <p className="text-sm " className="mr-4">
            Síguenos en redes sociales:
          </p>
          <p className="text-sm">

          </p>
          <a href="https://twitter.com/UNPet2023" target="_blank" rel="noopener noreferrer" className="mr-4">
            <FaTwitter className="h-6 w-6" />
          </a>
          <a href="https://www.instagram.com/unpet2023/" target="_blank" rel="noopener noreferrer">
            <FaInstagram className="h-6 w-6" />
          </a>
          <a href="https://www.facebook.com/profile.php?id=61552993962943" target="_blank" rel="noopener noreferrer" className="ml-4">
            <FaFacebook className="h-6 w-6" />
          </a>
        </div>
      </div>
    </footer>
  );
}
