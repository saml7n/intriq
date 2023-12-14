import { Head } from '~/components/shared/Head';
import { FlexibleXYPlot, LineSeries, ArcSeries, XAxis, YAxis } from 'react-vis';
import '~/../node_modules/react-vis/dist/style.css';
import { IoMailOutline } from 'react-icons/io5';
import { useNavigation } from '~/lib/NavigationContext';
import { useState } from 'react';

interface NavigationLinkProps {
  stepIndex: number;
  url: string;
}
const DataSourceRow: React.FC<NavigationLinkProps> = ({ url, stepIndex }) => {
  return (
    <></>
  );
};

function DataConnect() {
  const [addDataSourceOpen, setAddDataSourceOpen] = useState<boolean>(false);

  const { completedStep, setCompletedStep } = useNavigation();
  function onClickHandler(event: any): void {
    if (completedStep < 2) setCompletedStep(2);
  }

  return (
    <>
      <Head title="Connect Data" />
      <div className="bg-base-100 text-base-content sticky top-0 z-30 flex h-16 w-full justify-center bg-opacity-90 backdrop-blur transition-shadow duration-100 [transform:translate3d(0,0,0)] shadow-sm">
        <nav className="navbar w-full sticky bg-base-100 top-0 z-30 flex items-center plr-2 gap-2 lg:gap-4">
          <span className="tooltip tooltip-bottom before:text-xs before:content-[attr(data-tip)]">
            <label
              aria-label="Open menu"
              htmlFor="my-drawer"
              className="btn btn-square btn-ghost drawer-button lg:hidden "
            >
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
            <h1 className="lg:text-2xl lg:font-light">Connect Data</h1>
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
          <div tabIndex={0} className="collapse bg-base-200">
            <div className="collapse-title text-xl font-medium">
              <button className="form-control btn btn-primary" onClick={onClickHandler}>
                Add new Data Source
              </button>
            </div>
            <div className="collapse-content">
              <p>tabIndex={0} attribute is necessary to make the div focusable</p>
            </div>
          </div>

          <hr className="my-6 border-t-2 border-base-content/5" />
          <div className="overflow-x-auto">
            <table className="table table-zebra">
              {/* head */}
              <thead>
                <tr>
                  <th>
                    <label>
                      <input type="checkbox" className="checkbox" />
                    </label>
                  </th>
                  <th>Name</th>
                  <th>Type</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {/* row 3 */}
                <tr className="hover">
                  <th>
                    <label>
                      <input type="checkbox" className="checkbox" />
                    </label>
                  </th>
                  <td>
                    <div className="flex items-center gap-3">
                      <div className="avatar">
                        <div className="mask mask-squircle w-12 h-12">
                          <img src="https://picsum.photos/80/80?5" alt="Avatar Tailwind CSS Component" />
                        </div>
                      </div>
                      <div>
                        <div className="font-bold">Marjy Ferencz</div>
                        <div className="text-sm opacity-50">Russia</div>
                      </div>
                    </div>
                  </td>
                  <td>
                    Rowe-Schoen
                    <br />
                    <span className="badge badge-ghost badge-sm">Office Assistant I</span>
                  </td>
                  <th>
                    <button className="btn btn-ghost btn-xs">details</button>
                  </th>
                </tr>
                {/* row 4 */}
                <tr className="hover">
                  <th>
                    <label>
                      <input type="checkbox" className="checkbox" />
                    </label>
                  </th>
                  <td>
                    <div className="flex items-center gap-3">
                      <div className="avatar">
                        <div className="mask mask-squircle w-12 h-12">
                          <img src="https://picsum.photos/80/80?5" alt="Avatar Tailwind CSS Component" />
                        </div>
                      </div>
                      <div>
                        <div className="font-bold">Yancy Tear</div>
                        <div className="text-sm opacity-50">Brazil</div>
                      </div>
                    </div>
                  </td>
                  <td>
                    Wyman-Ledner
                    <br />
                    <span className="badge badge-ghost badge-sm">Community Outreach Specialist</span>
                  </td>
                  <th>
                    <button className="btn btn-ghost btn-xs">details</button>
                  </th>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
      </div>
    </>
  );
}

export default DataConnect;
