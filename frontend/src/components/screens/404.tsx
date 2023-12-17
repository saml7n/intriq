import {Head} from "~/components/shared/Head";
import { isRouteErrorResponse, useNavigate, useRouteError } from "react-router-dom";

function Page404() {
  const navigate = useNavigate();
  const error = useRouteError();
  let errorMessage = '';
  if (isRouteErrorResponse(error)) {
    // error is type `ErrorResponse`
    errorMessage = error.error?.message || error.statusText;
  } else if (error instanceof Error) {
    errorMessage = error.message;
  } else if (typeof error === 'string') {
    errorMessage = error;
  } else {
    console.error(error);
    errorMessage = 'Unknown error';
  }

  return (
    <>
      <Head title={'The page is not found'}></Head>
      <div className="hero min-h-screen bg-gray-800">
        <div className="text-center hero-content text-3xl font-bold">
          <div>
            <h1>
              {errorMessage}
            </h1>
            <div className='mt-4'>
              <a className='link-primary cursor-pointer' onClick={() => navigate('/')}>Top Page</a>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default Page404
