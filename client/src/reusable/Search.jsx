function Search({ handleChange, search }) {
  return (
    <div className="bg-amber-400 py-3 px-6 ">
      <form>
        <label className="mr-5" htmlFor="search">
          Search for your favorites!
        </label>
        <input
          className="rounded-md"
          style={{ width: "275px" }}
          type="text"
          id="search"
          name="search"
          value={search}
          onChange={(e) => handleChange(e)}
        />
      </form>
    </div>
  );
}

export default Search;
