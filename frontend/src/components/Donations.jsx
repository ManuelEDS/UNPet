import { FaCreditCard } from 'react-icons/fa';
export function Donations() {
  return (
    <div className="bg-gray-100">
      <div className="max-w-7xl mx-auto py-16 px-4 sm:py-24 sm:px-6 lg:px-8">
        <div className="max-w-lg mx-auto md:max-w-none md:grid md:grid-cols-2 md:gap-8">
          <div>
            <h2 className="text-2xl font-extrabold text-gray-900 sm:text-3xl">
              Ayúdanos a dar más oportunidades
            </h2>
            <p className="mt-3 text-lg text-gray-500">
              Tu donación nos ayuda a seguir trabajando por los derechos de los animales.
            </p>
            <dl className="mt-8 space-y-6">
              <dt className="sr-only">Credit Card</dt>
              <dd className="flex justify-between bg-white rounded-md p-6">
              <FaCreditCard className="h-12 w-12 text-gray-400" aria-hidden="true" />           
                   <div className="ml-4 flex flex-col justify-between">
                  <div className="text-lg font-medium text-gray-900">Donar con tarjeta de crédito</div>
                  <p className="mt-2 text-sm text-gray-500">
                    Puedes hacer tu donación con tarjeta de crédito a través de nuestro sitio web.
                  </p>
                  <a href="#" className="mt-6 inline-flex items-center px-4 py-2 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700">
                    Donar ahora
                  </a>
                </div>
              </dd>
            </dl>
          </div>
          <div className="mt-12 sm:mt-16 md:mt-0">
            <h2 className="text-2xl font-extrabold text-gray-900 sm:text-3xl">
              Otras formas de donar
            </h2>
            <div className="mt-8">
              <div className="flow-root">
                <ul className="-my-5 divide-y divide-gray-200">
                  <li className="py-4">
                    <div className="flex items-center space-x-4">
                      <div className="flex-shrink-0">
                        <img className="h-8 w-8 rounded-full" src="https://tailwindui.com/img/logos/workcation-logo-indigo-600-mark-gray-800-and-indigo-600-text.svg" alt="" />
                      </div>
                      <div className="flex-1 min-w-0">
                        <a href="#" className="focus:outline-none">
                          <span className="absolute inset-0" aria-hidden="true" />
                          <p className="text-sm font-medium text-gray-900 truncate">Donar con PayPal</p>
                          <p className="text-sm text-gray-500 truncate">Puedes hacer tu donación con PayPal.</p>
                        </a>
                      </div>
                      <div>
                        <a href="#" className="flex-shrink-0 text-sm font-medium text-indigo-600 hover:text-indigo-500">
                          Donar ahora
                        </a>
                      </div>
                    </div>
                  </li>
                  <li className="py-4">
                    <div className="flex items-center space-x-4">
                      <div className="flex-shrink-0">
                        <img className="h-8 w-8 rounded-full" src="https://tailwindui.com/img/logos/tuple-logo-indigo-600-mark-gray-800-and-indigo-600-text.svg" alt="" />
                      </div>
                      <div className="flex-1 min-w-0">
                        <a href="#" className="focus:outline-none">
                          <span className="absolute inset-0" aria-hidden="true" />
                          <p className="text-sm font-medium text-gray-900 truncate">Donar con Nequi</p>
                          <p className="text-sm text-gray-500 truncate">Puedes hacer tu donación con Nequi.</p>
                        </a>
                      </div>
                      <div>
                        <a href="#" className="flex-shrink-0 text-sm font-medium text-indigo-600 hover:text-indigo-500">
                          Donar ahora
                        </a>
                      </div>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}