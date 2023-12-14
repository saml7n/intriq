import { Head } from '~/components/shared/Head';
import { FlexibleXYPlot, LineSeries, ArcSeries, XAxis, YAxis } from 'react-vis';
import '~/../node_modules/react-vis/dist/style.css';
import { IoMailOutline } from 'react-icons/io5';
import { useNavigation } from '~/lib/NavigationContext';

function CompanySetup() {
  const { completedStep, setCompletedStep } = useNavigation();
  function onClickHandler(event: any): void {
    if (completedStep < 1) setCompletedStep(1);
  }

  return (
    <>
      <Head title="Setup Company" />
      <div className="bg-base-100 text-base-content sticky top-0 z-30 flex h-16 w-full justify-center bg-opacity-90 backdrop-blur transition-shadow duration-100 [transform:translate3d(0,0,0)] shadow-sm">
        <nav className="navbar w-full sticky bg-base-100 top-0 z-30 flex items-center plr-2 gap-2 lg:gap-4">
          <span className="tooltip tooltip-bottom before:text-xs before:content-[attr(data-tip)]">
            <label aria-label="Open menu" htmlFor="my-drawer" className="btn btn-square btn-ghost drawer-button lg:hidden ">
              <svg
                width="20"
                height="20"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                className="inline-block h-5 w-5 stroke-current md:h-6 md:w-6"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M4 6h16M4 12h16M4 18h16"
                ></path>
              </svg>
            </label>
          </span>
          <div className="grow">
            <h1 className="lg:text-2xl lg:font-light">Setup Company</h1>
          </div>
          <div>
            <input type="text" placeholder="Search" className="input input-sm rounded-full max-sm:w-24" />
          </div>
          <div className="dropdown-end dropdown z-10">
            <div tabIndex={0} className="avatar btn btn-circle btn-ghost">
              <div className="w-10 rounded-full">
                <img src="https://picsum.photos/80/80?5" />
              </div>
            </div>
            <ul tabIndex={0} className="menu dropdown-content mt-3 w-52 rounded-box bg-base-100 p-2 shadow-2xl">
              <li>
                <a>Settings</a>
              </li>
              <li>
                <a>Logout</a>
              </li>
            </ul>
          </div>
        </nav>
      </div>
      <div className="grid grid-cols-12 grid-rows-[min-content] gap-y-12 p-4 lg:gap-x-12 lg:p-10">
        <section className="col-span-12 xl:col-span-4">
          <div className="form-control">
            <label className="label">
              <span className="label-text">Company name</span>
            </label>
            <input type="text" placeholder="Type here" className="input input-bordered" />
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Company Type</span>
            </label>
            <select className="select select-bordered">
              <option disabled selected>
                Pick
              </option>
              <option>Public</option>
              <option>Private</option>
              <option>StartUp</option>
              <option>Financial Institution</option>
            </select>
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Sector</span>
            </label>
            <input type="text" placeholder="Type here" className="input input-bordered" />
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Valuation $ millions</span>
            </label>
            <input type="range" min="1" max="100" value="25" className="range" step="25" />
            <div className="flex w-full justify-between px-2 py-2 text-xs">
              <span>1</span>
              <span>25</span>
              <span>50</span>
              <span>75</span>
              <span>100</span>
            </div>
          </div>
          <hr className="my-6 border-t-2 border-base-content/5" />
          <div className="form-control">
            <label className="label">
              <span className="label-text">Key KPIs (comma-separated)</span>
            </label>
            <textarea placeholder="Type here" className="textarea textarea-bordered" />
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Strategic goal</span>
            </label>
            <textarea placeholder="Type here" className="textarea textarea-bordered" />
          </div>
          <hr className="my-6 border-t-2 border-base-content/5" />
          <button className="btn btn-primary" onClick={onClickHandler}>{`${
            completedStep >= 1 ? 'Save' : 'Add'
          } Company`}</button>
        </section>
      </div>
    </>
  );
}

export default CompanySetup;
