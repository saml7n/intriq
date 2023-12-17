import { Head } from '~/components/shared/Head';
import { FlexibleXYPlot, LineSeries, ArcSeries, XAxis, YAxis } from 'react-vis';
import '~/../node_modules/react-vis/dist/style.css';
import { IoMailOutline } from 'react-icons/io5';
import { useNavigation } from '~/lib/NavigationContext';
import Navbar from '../shared/Navbar';
import { ChangeEvent, SyntheticEvent, useEffect, useState } from 'react';
import { DefaultService as api, Company } from '~/lib/client';
import { redirect, useLoaderData, useNavigate } from 'react-router-dom';

const defaultCompany: Company = {
  name: '',
  sector: '',
  valuation: 1,
  id: 0,
  type: '',
  kpi: '',
  goal: '',
  triplet_id: [],
  embedding_id: [],
};

type Toast = {
  title: string;
  type: 'info' | 'success' | 'error' | 'warning';
};

function CompanySetup() {
  const { completedStep, setCompletedStep, setActiveStep } = useNavigation();
  const navigate = useNavigate();
  const [company, setCompany] = useState<Company>((useLoaderData() as Company) || defaultCompany);
  const [toast, setToast] = useState<Toast | null>();
  async function onClickHandler(event: any) {
    await api.createCompanyCompanyPost(company).then((id) => {console.log(id); navigate(`/setup-company/${id}`)});
    if (completedStep < 1) setCompletedStep(1);
  }

  useEffect(() => {
    setActiveStep(1);
  }, []);

  function onNameChangeHandler(event: ChangeEvent<HTMLInputElement>): void {
    setCompany((company) => ({ ...company, name: event.target.value }));
  }

  function onValuationChangeHandler(event: ChangeEvent<HTMLInputElement>): void {
    setCompany((company) => ({ ...company, valuation: Math.max(parseInt(event.target.value) || 1, 1) }));
  }

  function onSectorChangeHandler(event: ChangeEvent<HTMLInputElement>): void {
    setCompany((company) => ({ ...company, sector: event.target.value }));
  }

  function onKPIChangeHandler(event: ChangeEvent<HTMLTextAreaElement>): void {
    setCompany((company) => ({ ...company, kpi: event.target.value }));
  }

  function onGoalChangeHandler(event: ChangeEvent<HTMLTextAreaElement>): void {
    setCompany((company) => ({ ...company, goal: event.target.value }));
  }

  function onTypeChangeHandler(event: ChangeEvent<HTMLSelectElement>): void {
    setCompany((company) => ({ ...company, type: event.target.value }));
  }

  return (
    <>
      <Head title="Setup Company" />
      <Navbar title="Setup Company" />
      <div className="grid grid-cols-12 grid-rows-[min-content] gap-y-12 p-4 lg:gap-x-12 lg:p-10">
        <section className="col-span-12 xl:col-span-8">
          <div className="form-control">
            <label className="label">
              <span className="label-text">Company name</span>
            </label>
            <input
              type="text"
              value={company.name}
              onChange={onNameChangeHandler}
              placeholder="Type here"
              className="input input-bordered"
            />
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Company Type</span>
            </label>
            <select className="select select-bordered" value={company.type} onChange={onTypeChangeHandler}>
              <option disabled value={''}>
                Pick
              </option>
              <option value={'public'}>Public</option>
              <option value={'private'}>Private</option>
              <option value={'startUp'}>StartUp</option>
              <option value={'financialInstitution'}>Financial Institution</option>
            </select>
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Sector</span>
            </label>
            <input
              type="text"
              placeholder="Type here"
              className="input input-bordered"
              value={company.sector}
              onChange={onSectorChangeHandler}
            />
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Valuation $ millions</span>
            </label>
            <input
              type="range"
              min="0"
              max="100"
              value={company.valuation}
              className="range"
              step="10"
              onChange={onValuationChangeHandler}
            />
            <div className="flex w-full justify-between px-2 py-2 text-xs">
              <span>1</span>
              <span>20</span>
              <span>40</span>
              <span>60</span>
              <span>80</span>
              <span>100</span>
            </div>
          </div>
          <hr className="my-6 border-t-2 border-base-content/5" />
          <div className="form-control">
            <label className="label">
              <span className="label-text">Key KPIs (comma-separated)</span>
            </label>
            <textarea
              placeholder="Type here"
              className="textarea textarea-bordered"
              value={company.kpi}
              onChange={onKPIChangeHandler}
            />
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Strategic goal</span>
            </label>
            <textarea
              placeholder="Type here"
              className="textarea textarea-bordered"
              value={company.goal}
              onChange={onGoalChangeHandler}
            />
          </div>
          <hr className="my-6 border-t-2 border-base-content/5" />
          <button className="btn btn-primary" onClick={onClickHandler}>{`${
            completedStep >= 1 ? 'Save' : 'Add'
          } Company`}</button>
        </section>
      </div>
      {toast && 
        <div className="toast">
          <div className={`alert alert-${toast.type}`}>
            <span>{toast.title}</span>
          </div>
        </div>
      }
    </>
  );
}

export default CompanySetup;
