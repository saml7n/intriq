import { Head } from '~/components/shared/Head';
import { FlexibleXYPlot, LineSeries, ArcSeries, XAxis, YAxis } from 'react-vis';
import '~/../node_modules/react-vis/dist/style.css';
import { IoMailOutline } from 'react-icons/io5';
import { useNavigation } from '~/lib/NavigationContext';
import Navbar from '../shared/Navbar';

function CompanySetup() {
  const { completedStep, setCompletedStep } = useNavigation();
  function onClickHandler(event: any): void {
    if (completedStep < 1) setCompletedStep(1);
  }

  return (
    <>
      <Head title="Setup Company" />
      <Navbar/>
      <div className="grid grid-cols-12 grid-rows-[min-content] gap-y-12 p-4 lg:gap-x-12 lg:p-10">
        <section className="col-span-12 xl:col-span-8">
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
