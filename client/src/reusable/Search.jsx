function Search({ handleChange, search }) {
  return (
    <div>
      <form>
        <label htmlFor="search">Search for your favorites!</label>
        <input
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
