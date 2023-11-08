// eslint-disable-next-line no-unused-vars

import { FaCreditCard } from 'react-icons/fa';

export function Donations() {
  return (
      <div className="w-1/2 md:w-1/2 lg:w-1/3 xl:w-1/4 mx-auto">
        <div className="mt-8 flex flex-col items-center">
          <div className="m-auto mt-8 shadow-lg w-96 bg-white rounded-lg overflow-hidden">
            <div className="p-4">
              <div className="flex flex-col items-center">
                <FaCreditCard className="text-primary text-6xl" />
                <h1 className=" font-bold mt-4 mb-2 text-lg text-center">
                  Ayúdanos a dar más oportunidades
                </h1>
              </div>
              <div className="flex flex-col items-center">
                <div class="flex flex-wrap">
                  <div class="w-full sm:w-1/2">
                    <div className="p-4">
                      <a href="https://paypal.me/UNPetDonaciones" target="_blank" rel="noopener noreferrer">
                        <img src={'paypal.png?url'} alt="Paypal"  />
                      </a>
                    </div>
                  </div>
                  <div class="w-full sm:w-1/2">
                    <div className="p-4">
                      <img src={'nequi.png?url'} alt="Nequi" />
                      <p className="text-lg mt-2">
                        Nequi - Juan Ramirez
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
  );
}
