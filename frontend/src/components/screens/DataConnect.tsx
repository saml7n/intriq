import { Head } from '~/components/shared/Head';
import '~/../node_modules/react-vis/dist/style.css';
import { useNavigate } from 'react-router-dom';
import Navbar from '../shared/Navbar';
import { useNavigation } from '~/lib/NavigationContext';
import { useEffect } from 'react';
import { BsThreeDots } from 'react-icons/bs';

interface DataSourceRowProps {
  name: string;
  type: string;
}
const DataSourceRow: React.FC<DataSourceRowProps> = ({ name, type }) => {
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
            <div className="text-sm opacity-50">{type}</div>
          </div>
        </div>
      </td>
      <td>
        tbd
        <br />
        <span className="badge badge-ghost badge-sm">tbd badge</span>
      </td>
      <th>
        <button className="btn btn-square btn-outline btn-xs">
          <BsThreeDots />
        </button>
      </th>
    </tr>
  );
};

function DataConnect() {
  const navigate = useNavigate();
  const { setActiveStep } = useNavigation();
  function onClickHandler(event: any): void {
    navigate('/connect-data/add');
  }

  useEffect(() => {
    setActiveStep(2);
  }, []);

  return (
    <>
      <Head title="Connect Data" />
      <Navbar title="Connect Data" />
      <div className="grid grid-cols-12 grid-rows-[min-content] gap-y-12 p-4 lg:gap-x-12 lg:p-10">
        <section className="col-span-12 xl:col-span-6">
          <button className="form-control btn btn-primary" onClick={onClickHandler}>
            Add new Data Source
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
                  <th>Name</th>
                  <th>Type</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                <DataSourceRow name="SAP Connection" type="automatic loader" />
                <DataSourceRow name="financial statement" type="document" />
              </tbody>
            </table>
          </div>
        </section>
      </div>
    </>
  );
}

export default DataConnect;
