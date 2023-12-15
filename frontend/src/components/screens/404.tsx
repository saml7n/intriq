import {Head} from "~/components/shared/Head";
import { useNavigate } from "react-router-dom";

function Page404() {
  const navigate = useNavigate();
  return (
    <>
      <Head title={'The page is not found'}></Head>
      <div className="hero min-h-screen bg-gray-800">
        <div className="text-center hero-content text-3xl font-bold">
          <div>
            <h1>
              The page is not found.
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
