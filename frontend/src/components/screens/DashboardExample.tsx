import { Head } from '~/components/shared/Head';
import { FlexibleXYPlot, LineSeries, ArcSeries, XAxis, YAxis } from 'react-vis';
import '~/../node_modules/react-vis/dist/style.css';
import { IoMailOutline } from 'react-icons/io5';

function Index() {
  const COLORS = [
    '#FFBD3C',
    '#3C37FF',
    '#A838FF',
    '#19D6BF',
    '#19CDD7',
    '#DDB27C',
    '#88572C',
    '#FF991F',
    '#F15C17',
    '#223F9A',
    '#DA70BF',
    '#125C77',
    '#4DC19C',
    '#776E57',
    '#12939A',
    '#17B8BE',
    '#F6D18A',
    '#B7885E',
    '#FFCB99',
    '#F89570',
    '#829AE3',
    '#E79FD5',
    '#1E96BE',
    '#89DAC1',
    '#B3AD9E',
  ];

  const data = [
    { x: 0, y: 2 },
    { x: 1, y: 5 },
    { x: 2, y: 4 },
    { x: 3, y: 6 },
    { x: 4, y: 1 },
    { x: 5, y: 3 },
    { x: 6, y: 6 },
    { x: 7, y: 5 },
    { x: 8, y: 7 },
    { x: 9, y: 9 },
  ];

  const myData = [
    { x: 'A', y: 10 },
    { x: 'B', y: 5 },
    { x: 'C', y: 15 },
  ];

  const myDataArc = [
    { angle0: (0 * Math.PI) / 4, angle: (3.5 * Math.PI) / 4, radius: 2, radius0: 0, color: 0 },
    { angle0: (3.5 * Math.PI) / 4, angle: (5.5 * Math.PI) / 4, radius: 2, radius0: 0, color: 1 },
    { angle0: (5.5 * Math.PI) / 4, angle: (6.2 * Math.PI) / 4, radius: 2, radius0: 0, color: 2 },
    { angle0: (6.2 * Math.PI) / 4, angle: (6.5 * Math.PI) / 4, radius: 2, radius0: 0, color: 3 },
  ];

  return (
    <>
      <Head title="Dashboard" />
      <div className="grid grid-cols-12 grid-rows-[min-content] gap-y-12 p-4 lg:gap-x-12 lg:p-10">
        <header className="col-span-12 flex items-center gap-2 lg:gap-4">
          <label htmlFor="my-drawer" className="btn btn-circle swap swap-rotate drawer-button lg:hidden">
            <input type="checkbox" />

            <svg
              className="swap-off fill-current"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 512 512"
            >
              <path d="M64,384H448V341.33H64Zm0-106.67H448V234.67H64ZM64,128v42.67H448V128Z" />
            </svg>

            <svg
              className="swap-on fill-current"
              xmlns="http://www.w3.org/2000/svg"
              width="32"
              height="32"
              viewBox="0 0 512 512"
            >
              <polygon points="400 145.49 366.51 112 256 222.51 145.49 112 112 145.49 222.51 256 112 366.51 145.49 400 256 289.49 366.51 400 400 366.51 289.49 256 400 145.49" />
            </svg>
          </label>
          <div className="grow">
            <h1 className="lg:text-2xl lg:font-light">Dashboard</h1>
          </div>
          <div>
            <input type="text" placeholder="Search" className="input input-sm rounded-full max-sm:w-24" />
          </div>
          <div className="dropdown dropdown-end z-10">
            <div tabIndex={0} className="btn btn-circle btn-ghost">
              <div className="indicator">
                <span className="badge indicator-item badge-error badge-xs"></span>
                <IoMailOutline className="scale-150" />
              </div>
            </div>
            <ul tabIndex={0} className="menu dropdown-content mt-3 w-80 rounded-box bg-base-100 p-2 shadow-2xl">
              <li>
                <a className="gap-4">
                  <div className="avatar">
                    <div className="w-8 rounded-full">
                      <img src="https://picsum.photos/80/80?1" />
                    </div>
                  </div>
                  <span>
                    <b>New message</b>
                    <br />
                    Alice: Hi, did you get my files?
                  </span>
                </a>
              </li>
              <li>
                <a className="gap-4">
                  <div className="avatar">
                    <div className="w-8 rounded-full">
                      <img src="https://picsum.photos/80/80?2" />
                    </div>
                  </div>
                  <span>
                    <b>Reminder</b>
                    <br />
                    Your meeting is at 10am
                  </span>
                </a>
              </li>
              <li>
                <a className="gap-4">
                  <div className="avatar">
                    <div className="w-8 rounded-full">
                      <img src="https://picsum.photos/80/80?3" />
                    </div>
                  </div>
                  <span>
                    <b>New payment</b>
                    <br />
                    Received $2500 from John Doe
                  </span>
                </a>
              </li>
              <li>
                <a className="gap-4">
                  <div className="avatar">
                    <div className="w-8 rounded-full">
                      <img src="https://picsum.photos/80/80?4" />
                    </div>
                  </div>
                  <span>
                    <b>New payment</b>
                    <br />
                    Received $1900 from Alice
                  </span>
                </a>
              </li>
            </ul>
          </div>
          <div className="dropdown-end dropdown z-10">
            <div tabIndex={0} className="avatar btn btn-circle btn-ghost">
              <div className="w-10 rounded-full">
                <img src="https://picsum.photos/80/80?5" />
              </div>
            </div>
            <ul tabIndex={0} className="menu dropdown-content mt-3 w-52 rounded-box bg-base-100 p-2 shadow-2xl">
              <li>
                <a>Profile</a>
              </li>
              <li>
                <a>
                  Inbox
                  <span className="badge badge-success">12</span>
                </a>
              </li>
              <li>
                <a>Settings</a>
              </li>
              <li>
                <a>Logout</a>
              </li>
            </ul>
          </div>
        </header>
        <section className="stats stats-vertical col-span-12 w-full shadow-sm xl:stats-horizontal">
          <div className="stat">
            <div className="stat-title">Total Page Views</div>
            <div className="stat-value">89,400</div>
            <div className="stat-desc">21% more than last month</div>
          </div>

          <div className="stat">
            <div className="stat-title">Total Page Views</div>
            <div className="stat-value">89,400</div>
            <div className="stat-desc">21% more than last month</div>
          </div>

          <div className="stat">
            <div className="stat-title">Total Page Views</div>
            <div className="stat-value">89,400</div>
            <div className="stat-desc">21% more than last month</div>
          </div>

          <div className="stat">
            <div className="stat-title">Total Page Views</div>
            <div className="stat-value">89,400</div>
            <div className="stat-desc">21% more than last month</div>
          </div>
        </section>
        <section className="card col-span-12 overflow-hidden bg-base-100 shadow-sm xl:col-span-6">
          <div className="card-body grow-0">
            <h2 className="card-title">
              <a className="link-hover link">Transactions</a>
            </h2>
          </div>
          <div className="overflow-x-auto">
            <table className="table table-zebra">
              <tbody>
                <tr>
                  <td>Cy Ganderton</td>
                  <td>Feb 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-up-right.svg"
                      className="inline-block h-5 w-5 text-success"
                    ></svg>
                    180 USD
                  </td>
                </tr>
                <tr>
                  <td>Hart Hagerty</td>
                  <td>Sep 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-up-right.svg"
                      className="inline-block h-5 w-5 text-success"
                    ></svg>
                    250 USD
                  </td>
                </tr>
                <tr>
                  <td>Jim Hagerty</td>
                  <td>Sep 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-up-right.svg"
                      className="inline-block h-5 w-5 text-success"
                    ></svg>
                    250 USD
                  </td>
                </tr>
                <tr>
                  <td>Hart Hagerty</td>
                  <td>Sep 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-down-right.svg"
                      className="inline-block h-5 w-5 text-error"
                    ></svg>
                    250 USD
                  </td>
                </tr>
                <tr>
                  <td>Hart Hagerty</td>
                  <td>Sep 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-down-right.svg"
                      className="inline-block h-5 w-5 text-error"
                    ></svg>
                    250 USD
                  </td>
                </tr>
                <tr>
                  <td>Brice Swyre</td>
                  <td>Jul 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-up-right.svg"
                      className="inline-block h-5 w-5 text-success"
                    ></svg>
                    320 USD
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
        <section className="card pr-0.5 col-span-12 bg-primary text-primary-content shadow-sm xl:col-span-6 min-h-[300px]">
          <div className="card-body pb-0">
            <h2 className="card-title">21,500 USD</h2>
            <a className="link-hover link text-xs">Revenue report →</a>
          </div>
          <FlexibleXYPlot>
            <XAxis
              style={{
                line: { stroke: 'oklch(var(--pc))' },
                ticks: { stroke: 'oklch(var(--pc))' },
                text: { stroke: 'none', fill: 'oklch(var(--pc))', fontWeight: 600 },
              }}
            />
            <YAxis
              style={{
                line: { stroke: 'oklch(var(--pc))' },
                ticks: { stroke: 'oklch(var(--pc))' },
                text: { stroke: 'none', fill: 'oklch(var(--pc))', fontWeight: 600 },
              }}
            />
            <LineSeries data={data} />
          </FlexibleXYPlot>
          {/*<TcColumn
              className="h-full w-full p-4 pt-0 [--shape-color:oklch(var(--pc))]"
              values="[12,10,12,4,13,16,14,10,12,11,17,18,16,17,20,14,15,13,12,14]"
              min="0"
              shape-radius="4"
              shape-gap="4"
            ></TcColumn>*/}
        </section>
        <section className="card col-span-12 bg-base-100 shadow-sm xl:col-span-4 min-h-[300px]">
          <div className="card-body">
            <h2 className="card-title">Sources</h2>
            <div className="flex items-center gap-10 h-full">
              <div className="grow">
                <div className="flex items-center gap-2">
                  <span className={`badge badge-xs bg-[${COLORS[0]}]`}></span>
                  Direct
                </div>
                <div className="flex items-center gap-2">
                  <span className={`badge badge-xs bg-[${COLORS[1]}]`}></span>
                  Social
                </div>
                <div className="flex items-center gap-2">
                  <span className={`badge badge-xs bg-[${COLORS[2]}]`}></span>
                  Search
                </div>
                <div className="flex items-center gap-2">
                  <span className={`badge badge-xs bg-[${COLORS[3]}]`}></span>
                  Email
                </div>
              </div>
              <FlexibleXYPlot xDomain={[-3, 3]} yDomain={[-3, 3]} colorType={'category'} colorDomain={[0, 1, 2]}>
                <ArcSeries data={myDataArc} colorRange={COLORS} />
              </FlexibleXYPlot>
            </div>
          </div>
        </section>
        <section className="card col-span-12 bg-base-100 shadow-sm xl:col-span-4 min-h-[300px]">
          <div className="card-body pb-0">
            <h2 className="card-title">19,000</h2>
            <p>Downloads</p>
          </div>
          <FlexibleXYPlot>
            <XAxis />
            <YAxis />
            <LineSeries data={data} />
          </FlexibleXYPlot>
        </section>
        <section className="card col-span-12 bg-base-100 shadow-sm xl:col-span-4 min-h-[300px]">
          <div className="card-body pb-0">
            <h2 className="card-title">32,800</h2>
            <p>Unique visitors</p>
          </div>
          <FlexibleXYPlot>
            <XAxis />
            <YAxis />
            <LineSeries data={data} />
          </FlexibleXYPlot>
        </section>
        <header className="col-span-12 flex items-center gap-2 lg:gap-4">
          <div className="grow">
            <h1 className="font-light lg:text-2xl">Forms and inputs</h1>
          </div>
        </header>
        <section className="col-span-12 xl:col-span-4">
          <div className="form-control">
            <label className="label">
              <span className="label-text">Product name</span>
            </label>
            <input type="text" placeholder="Type here" className="input input-bordered" />
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Category</span>
            </label>
            <select className="select select-bordered">
              <option disabled selected>
                Pick
              </option>
              <option>T-shirts</option>
              <option>Dresses</option>
              <option>Hats</option>
              <option>Accessories</option>
            </select>
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Size (cm)</span>
            </label>
            <div className="flex items-center gap-2">
              <input type="text" placeholder="Width" className="input input-bordered w-1/2" />
              ×
              <input type="text" placeholder="Height" className="input input-bordered w-1/2" />
            </div>
          </div>
          <hr className="my-6 border-t-2 border-base-content/5" />
          <div className="form-control">
            <div className="label justify-start gap-2">
              <svg
                data-src="https://unpkg.com/heroicons/20/solid/eye.svg"
                className="h-4 w-4 text-base-content/30"
              ></svg>
              <span className="label-text text-xs font-bold text-base-content/50">Choose product visibility</span>
            </div>
          </div>
          <div className="form-control">
            <label className="label cursor-pointer">
              <span className="label-text">Visible only for managers</span>
              <input name="visibility" type="radio" className="radio radio-sm" checked />
            </label>
            <label className="label cursor-pointer">
              <span className="label-text">Visible for all users</span>
              <input name="visibility" type="radio" className="radio radio-sm" checked />
            </label>
          </div>
        </section>
        <section className="card col-span-12 bg-base-100 shadow-sm xl:col-span-3">
          <div className="p-6 pb-0 text-center text-xs font-bold text-base-content/60">Recent events</div>
          <ul className="menu">
            <li>
              <a className="gap-4">
                <div className="avatar">
                  <div className="w-6 rounded-full">
                    <img src="https://picsum.photos/80/80?6" />
                  </div>
                </div>
                <span className="text-xs">
                  <b>New User</b>
                  <br />2 minutes ago
                </span>
              </a>
            </li>
            <li>
              <a className="gap-4">
                <div className="avatar">
                  <div className="w-6 rounded-full">
                    <img src="https://picsum.photos/80/80?7" />
                  </div>
                </div>
                <span className="text-xs">
                  <b>New product added</b>
                  <br />1 hour ago
                </span>
              </a>
            </li>
            <li>
              <a className="gap-4">
                <div className="avatar">
                  <div className="w-6 rounded-full">
                    <img src="https://picsum.photos/80/80?8" />
                  </div>
                </div>
                <span className="text-xs">
                  <b>Database update</b>
                  <br />1 hour ago
                </span>
              </a>
            </li>
            <li>
              <a className="gap-4">
                <div className="avatar">
                  <div className="w-6 rounded-full">
                    <img src="https://picsum.photos/80/80?9" />
                  </div>
                </div>
                <span className="text-xs">
                  <b>Newsletter sent</b>
                  <br />2 hour ago
                </span>
              </a>
            </li>
            <li>
              <a className="gap-4">
                <div className="avatar">
                  <div className="w-6 rounded-full">
                    <img src="https://picsum.photos/80/80?10" />
                  </div>
                </div>
                <span className="text-xs">
                  <b>New User</b>
                  <br />2 hours ago
                </span>
              </a>
            </li>
            <li>
              <a className="gap-4">
                <div className="avatar">
                  <div className="w-6 rounded-full">
                    <img src="https://picsum.photos/80/80?11" />
                  </div>
                </div>
                <span className="text-xs">
                  <b>New product added</b>
                  <br />
                  yesterday
                </span>
              </a>
            </li>
            <li>
              <a className="gap-4">
                <div className="avatar">
                  <div className="w-6 rounded-full">
                    <img src="https://picsum.photos/80/80?12" />
                  </div>
                </div>
                <span className="text-xs">
                  <b>New product added</b>
                  <br />
                  yesterday
                </span>
              </a>
            </li>
          </ul>
        </section>
        <header className="col-span-12 flex items-center gap-2 lg:gap-4">
          <div className="grow">
            <h1 className="font-light lg:text-2xl">Form sections</h1>
          </div>
        </header>
        <section className="col-span-12 xl:col-span-4">
          <label className="label">
            <span className="label-text">Product management</span>
          </label>
          <ul className="flex flex-col gap-4 p-1">
            <li className="flex items-start gap-4">
              <img
                className="h-14 w-14 shrink-0 rounded-btn"
                width="56"
                height="56"
                src="https://picsum.photos/80/80?id=1"
                alt="Product"
              />
              <div className="flex grow flex-col gap-1">
                <div className="text-sm">Portable fidget spinner</div>
                <div className="text-xs text-base-content/50">Space Gray</div>
                <div className="font-mono text-xs text-base-content/50">$299</div>
              </div>
              <div className="join justify-self-end bg-base-100">
                <button className="btn btn-ghost join-item btn-xs">–</button>
                <input className="input join-item input-ghost input-xs w-10 text-center" value="1" />
                <button className="btn btn-ghost join-item btn-xs">+</button>
              </div>
            </li>
            <li className="flex items-start gap-4">
              <img
                className="h-14 w-14 shrink-0 rounded-btn"
                width="56"
                height="56"
                src="https://picsum.photos/80/80?id=2"
                alt="Product"
              />
              <div className="flex grow flex-col gap-1">
                <div className="text-sm">Wooden VR holder</div>
                <div className="text-xs text-base-content/50">Casual Red</div>
                <div className="font-mono text-xs text-base-content/50">$199</div>
              </div>
              <div className="join justify-self-end bg-base-100">
                <button className="btn btn-ghost join-item btn-xs">–</button>
                <input className="input join-item input-ghost input-xs w-10 text-center" value="1" />
                <button className="btn btn-ghost join-item btn-xs">+</button>
              </div>
            </li>
            <li className="flex items-start gap-4">
              <img
                className="h-14 w-14 shrink-0 rounded-btn"
                width="56"
                height="56"
                src="https://picsum.photos/80/80?id=3"
                alt="Product"
              />
              <div className="flex grow flex-col gap-1">
                <div className="text-sm">Portable keychain</div>
                <div className="text-xs text-base-content/50">Normal Yellow</div>
                <div className="font-mono text-xs text-base-content/50">$299</div>
              </div>
              <div className="join justify-self-end bg-base-100">
                <button className="btn btn-ghost join-item btn-xs">–</button>
                <input className="input join-item input-ghost input-xs w-10 text-center" value="1" />
                <button className="btn btn-ghost join-item btn-xs">+</button>
              </div>
            </li>
          </ul>
        </section>
        <section className="col-span-12 xl:col-span-4">
          <div className="form-control">
            <label className="label">
              <span className="label-text">Product name</span>
            </label>
            <input type="text" placeholder="Type here" className="input input-bordered" />
          </div>
          <div className="form-control">
            <label className="label">
              <span className="label-text">Category</span>
            </label>
            <select className="select select-bordered">
              <option disabled selected>
                Pick
              </option>
              <option>T-shirts</option>
              <option>Dresses</option>
              <option>Hats</option>
              <option>Accessories</option>
            </select>
          </div>

          <div className="form-control">
            <label className="label cursor-pointer">
              <span className="label-text">Public</span>
              <input type="checkbox" className="toggle toggle-sm" checked />
            </label>
          </div>
          <div className="form-control">
            <label className="label cursor-pointer">
              <span className="label-text">Featured product</span>
              <input type="checkbox" className="toggle toggle-sm" checked />
            </label>
          </div>
        </section>
        <section className="col-span-12 xl:col-span-4">
          <div className="form-control">
            <label className="label">
              <span className="label-text">Size (cm)</span>
            </label>
            <div className="flex items-center gap-2">
              <input type="text" placeholder="Width" className="input input-bordered w-1/2" />
              ×
              <input type="text" placeholder="Height" className="input input-bordered w-1/2" />
            </div>
          </div>
          <div className="form-control">
            <div className="py-4 text-xs text-base-content/70">
              Set a audience range for this product.
              <br />
              This is optional
            </div>
            <input type="range" min="0" max="100" value="25" className="range range-xs" step="25" />
            <div className="flex w-full justify-between px-2 py-2 text-xs">
              <span>0</span>
              <span>25</span>
              <span>50</span>
              <span>75</span>
              <span>100</span>
            </div>
          </div>
          <div className="form-control">
            <div className="flex gap-4 py-4">
              <button className="btn btn-outline">Save draft</button>
              <button className="btn btn-primary grow">Save and publish</button>
            </div>
          </div>
        </section>
        <header className="col-span-12 flex items-center gap-2 lg:gap-4">
          <div className="grow">
            <h1 className="font-light lg:text-2xl">Payment information</h1>
          </div>
        </header>
        <section className="card col-span-12 bg-base-100 xl:col-span-5">
          <form className="card-body" action="">
            <div className="alert alert-success">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-6 w-6 shrink-0 stroke-current"
                fill="none"
                viewBox="0 0 24 24"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
              <span>Your payment was successful</span>
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">Card Number</span>
              </label>
              <input
                type="text"
                className="input input-bordered font-mono"
                pattern="\d{16}"
                title="16 digits card number"
                minLength={16}
                maxLength={16}
                required
              />
            </div>
            <div className="grid grid-cols-2 gap-2">
              <div className="form-control">
                <label className="label">
                  <span className="label-text">CVV</span>
                </label>
                <input
                  type="text"
                  placeholder="XXX"
                  pattern="\d{3,4}"
                  title="3 or 4 digits CVV number"
                  minLength={3}
                  maxLength={4}
                  required
                  className="input input-bordered text-center font-mono"
                />
              </div>
              <div className="form-control">
                <label className="label">
                  <span className="label-text">Expiration date</span>
                </label>
                <div className="input input-bordered grid grid-cols-2 gap-2">
                  <input
                    placeholder="MM"
                    type="text"
                    pattern="\d{2}"
                    title="2 digits month number"
                    minLength={2}
                    maxLength={2}
                    className="text-center font-mono"
                    required
                  />
                  <input
                    placeholder="YY"
                    type="text"
                    pattern="\d{2}"
                    title="2 digits year number"
                    minLength={2}
                    maxLength={2}
                    className="text-center font-mono"
                    required
                  />
                </div>
              </div>
            </div>
            <div className="form-control">
              <label className="label">
                <span className="label-text">Name</span>
              </label>
              <input type="text" className="input input-bordered" />
            </div>
            <div className="form-control mt-4 gap-4">
              <label className="flex cursor-pointer gap-4">
                <input type="checkbox" className="checkbox checkbox-sm" checked />
                <span className="label-text">Save my card information for future payments</span>
              </label>
              <label className="flex cursor-pointer gap-4">
                <input required type="checkbox" className="checkbox checkbox-sm" checked />
                <span className="label-text">Accept terms of use and privac policy</span>
              </label>
            </div>
            <div className="form-control">
              <div className="flex items-end py-4">
                <button className="btn btn-primary grow">Confirm Payment</button>
              </div>
            </div>
          </form>
        </section>
        <section className="card col-span-12 overflow-hidden bg-base-100 shadow-sm xl:col-span-7">
          <div className="card-body grow-0">
            <div className="flex justify-between gap-2">
              <h2 className="card-title grow">
                <a className="link-hover link">Recent user transactions</a>
              </h2>
              <button className="btn btn-sm">See all users</button>
              <button className="btn btn-sm">Settings</button>
            </div>
          </div>
          <div className="overflow-x-auto">
            <table className="table table-zebra">
              <tbody>
                <tr>
                  <td className="w-0">
                    <input type="checkbox" className="checkbox" />
                  </td>
                  <td>
                    <div className="flex items-center gap-4">
                      <div className="avatar">
                        <div className="mask mask-squircle h-10 w-10">
                          <img src="https://picsum.photos/80/80?1" alt="Avatar Tailwind CSS Component" />
                        </div>
                      </div>
                      <div>
                        <div className="text-sm font-bold">Hart Hagerty</div>
                        <div className="text-xs opacity-50">United States</div>
                      </div>
                    </div>
                  </td>
                  <td>Feb 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-up-right.svg"
                      className="inline-block h-5 w-5 text-success"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                      aria-hidden="true"
                      data-id="svg-loader_3"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M5.22 14.78a.75.75 0 001.06 0l7.22-7.22v5.69a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75h-7.5a.75.75 0 000 1.5h5.69l-7.22 7.22a.75.75 0 000 1.06z"
                        clip-rule="evenodd"
                      ></path>
                    </svg>
                    180 USD
                  </td>
                </tr>
                <tr>
                  <td className="w-0">
                    <input type="checkbox" className="checkbox" />
                  </td>
                  <td>
                    <div className="flex items-center gap-4">
                      <div className="avatar">
                        <div className="mask mask-squircle h-10 w-10">
                          <img src="https://picsum.photos/80/80?2" alt="Avatar Tailwind CSS Component" />
                        </div>
                      </div>
                      <div>
                        <div className="text-sm font-bold">Brice Swyre</div>
                        <div className="text-xs opacity-50">China</div>
                      </div>
                    </div>
                  </td>
                  <td>Sep 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-up-right.svg"
                      className="inline-block h-5 w-5 text-success"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                      aria-hidden="true"
                      data-id="svg-loader_4"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M5.22 14.78a.75.75 0 001.06 0l7.22-7.22v5.69a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75h-7.5a.75.75 0 000 1.5h5.69l-7.22 7.22a.75.75 0 000 1.06z"
                        clip-rule="evenodd"
                      ></path>
                    </svg>
                    250 USD
                  </td>
                </tr>
                <tr>
                  <td className="w-0">
                    <input type="checkbox" className="checkbox" />
                  </td>
                  <td>
                    <div className="flex items-center gap-4">
                      <div className="avatar">
                        <div className="mask mask-squircle h-10 w-10">
                          <img src="https://picsum.photos/80/80?3" alt="Avatar Tailwind CSS Component" />
                        </div>
                      </div>
                      <div>
                        <div className="text-sm font-bold">Marjy Ferencz</div>
                        <div className="text-xs opacity-50">Russia</div>
                      </div>
                    </div>
                  </td>
                  <td>Sep 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-up-right.svg"
                      className="inline-block h-5 w-5 text-success"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                      aria-hidden="true"
                      data-id="svg-loader_5"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M5.22 14.78a.75.75 0 001.06 0l7.22-7.22v5.69a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75h-7.5a.75.75 0 000 1.5h5.69l-7.22 7.22a.75.75 0 000 1.06z"
                        clip-rule="evenodd"
                      ></path>
                    </svg>
                    250 USD
                  </td>
                </tr>
                <tr>
                  <td className="w-0">
                    <input type="checkbox" className="checkbox" />
                  </td>
                  <td>
                    <div className="flex items-center gap-4">
                      <div className="avatar">
                        <div className="mask mask-squircle h-10 w-10">
                          <img src="https://picsum.photos/80/80?4" alt="Avatar Tailwind CSS Component" />
                        </div>
                      </div>
                      <div>
                        <div className="text-sm font-bold">Yancy Tear</div>
                        <div className="text-xs opacity-50">Brazil</div>
                      </div>
                    </div>
                  </td>
                  <td>Sep 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-down-right.svg"
                      className="inline-block h-5 w-5 text-error"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                      aria-hidden="true"
                      data-id="svg-loader_6"
                    >
                      <path d="M6.28 5.22a.75.75 0 00-1.06 1.06l7.22 7.22H6.75a.75.75 0 000 1.5h7.5a.747.747 0 00.75-.75v-7.5a.75.75 0 00-1.5 0v5.69L6.28 5.22z"></path>
                    </svg>
                    250 USD
                  </td>
                </tr>
                <tr>
                  <td className="w-0">
                    <input type="checkbox" className="checkbox" />
                  </td>
                  <td>
                    <div className="flex items-center gap-4">
                      <div className="avatar">
                        <div className="mask mask-squircle h-10 w-10">
                          <img src="https://picsum.photos/80/80?5" alt="Avatar Tailwind CSS Component" />
                        </div>
                      </div>
                      <div>
                        <div className="text-sm font-bold">Marjy Ferencz</div>
                        <div className="text-xs opacity-50">Russia</div>
                      </div>
                    </div>
                  </td>
                  <td>Sep 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-down-right.svg"
                      className="inline-block h-5 w-5 text-error"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                      aria-hidden="true"
                      data-id="svg-loader_7"
                    >
                      <path d="M6.28 5.22a.75.75 0 00-1.06 1.06l7.22 7.22H6.75a.75.75 0 000 1.5h7.5a.747.747 0 00.75-.75v-7.5a.75.75 0 00-1.5 0v5.69L6.28 5.22z"></path>
                    </svg>
                    250 USD
                  </td>
                </tr>
                <tr>
                  <td className="w-0">
                    <input type="checkbox" className="checkbox" />
                  </td>
                  <td>
                    <div className="flex items-center gap-4">
                      <div className="avatar">
                        <div className="mask mask-squircle h-10 w-10">
                          <img src="https://picsum.photos/80/80?6" alt="Avatar Tailwind CSS Component" />
                        </div>
                      </div>
                      <div>
                        <div className="text-sm font-bold">Hart Hagerty</div>
                        <div className="text-xs opacity-50">United States</div>
                      </div>
                    </div>
                  </td>
                  <td>Jul 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-up-right.svg"
                      className="inline-block h-5 w-5 text-success"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                      aria-hidden="true"
                      data-id="svg-loader_8"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M5.22 14.78a.75.75 0 001.06 0l7.22-7.22v5.69a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75h-7.5a.75.75 0 000 1.5h5.69l-7.22 7.22a.75.75 0 000 1.06z"
                        clip-rule="evenodd"
                      ></path>
                    </svg>
                    320 USD
                  </td>
                </tr>

                <tr>
                  <td className="w-0">
                    <input type="checkbox" className="checkbox" />
                  </td>
                  <td>
                    <div className="flex items-center gap-4">
                      <div className="avatar">
                        <div className="mask mask-squircle h-10 w-10">
                          <img src="https://picsum.photos/80/80?1" alt="Avatar Tailwind CSS Component" />
                        </div>
                      </div>
                      <div>
                        <div className="text-sm font-bold">Hart Hagerty</div>
                        <div className="text-xs opacity-50">United States</div>
                      </div>
                    </div>
                  </td>
                  <td>Feb 2nd</td>
                  <td>
                    <svg
                      data-src="https://unpkg.com/heroicons/20/solid/arrow-up-right.svg"
                      className="inline-block h-5 w-5 text-success"
                      xmlns="http://www.w3.org/2000/svg"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                      aria-hidden="true"
                      data-id="svg-loader_3"
                    >
                      <path
                        fill-rule="evenodd"
                        d="M5.22 14.78a.75.75 0 001.06 0l7.22-7.22v5.69a.75.75 0 001.5 0v-7.5a.75.75 0 00-.75-.75h-7.5a.75.75 0 000 1.5h5.69l-7.22 7.22a.75.75 0 000 1.06z"
                        clip-rule="evenodd"
                      ></path>
                    </svg>
                    180 USD
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </section>
      </div>
    </>
  );
}

export default Index;
