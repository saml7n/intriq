import { Head } from '~/components/shared/Head';
import '~/../node_modules/react-vis/dist/style.css';
import { useNavigate } from 'react-router-dom';
import Navbar from '../shared/Navbar';
import { useNavigation } from '~/lib/NavigationContext';
import { useEffect } from 'react';
import { BsThreeDots } from 'react-icons/bs';
import { MdDownload } from 'react-icons/md';

type RAGStatus = 'red' | 'amber' | 'green';

//name="Digital Transformation" department='Technology' timeframe='1 year' status='In Progress' progress='30%' RAG='amber'
interface InitiativeRowProps {
  name: string;
  department: string;
  timeframe: string;
  status: string;
  progress: string;
  rag: RAGStatus;
}
const InitiativeRow: React.FC<InitiativeRowProps> = ({ name, department, timeframe, status, progress, rag }) => {
  return (
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
            <div className="font-bold">{name}</div>
            <div className="text-sm opacity-50">{department}</div>
          </div>
        </div>
      </td>
      <td>{timeframe}</td>
      <td>{status}</td>
      <td>{progress}</td>
      <td>
        <span
          className={`badge badge-xs ${rag === 'red' ? 'bg-error' : rag === 'amber' ? 'bg-warning' : 'bg-success'}`}
        ></span>
      </td>
      <th>
        <button className="btn btn-square btn-outline btn-xs">
          <BsThreeDots />
        </button>
      </th>
    </tr>
  );
};

function InitiativeTracking() {
  const navigate = useNavigate();
  const { setActiveStep } = useNavigation();
  function onClickHandler(event: any): void {}

  useEffect(() => {
    setActiveStep(4);
  }, []);

  return (
    <>
      <Head title="Track Initiatives" />
      <Navbar title="Track Initiatives" />
      <div className="grid grid-cols-12 grid-rows-[min-content] gap-y-12 p-4 lg:gap-x-12 lg:p-10">
        <section className="col-span-12 xl:col-span-6">
          <button className="btn btn-primary" onClick={onClickHandler}>
            <MdDownload transform="scale(1.4)" /> Generate Report
          </button>

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
                  <th>Initiative</th>
                  <th>Timeframe</th>
                  <th>Status</th>
                  <th>Progress</th>
                  <th>RAG</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <InitiativeRow
                  name="Digital Transformation"
                  department="Technology"
                  timeframe="1 year"
                  status="In Progress"
                  progress="30%"
                  rag="green"
                />
                <InitiativeRow
                  name="Digital Transformation"
                  department="Technology"
                  timeframe="1 year"
                  status="In Progress"
                  progress="30%"
                  rag="amber"
                />
                <InitiativeRow
                  name="Digital Transformation"
                  department="Technology"
                  timeframe="1 year"
                  status="In Progress"
                  progress="30%"
                  rag="red"
                />
              </tbody>
            </table>
          </div>
        </section>
      </div>
    </>
  );
}

export default InitiativeTracking;
