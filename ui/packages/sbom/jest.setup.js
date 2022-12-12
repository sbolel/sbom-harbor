/**
 * @module @cyclone-dx/ui/sbom/utils/setupTests
 */
import '@testing-library/jest-dom'
import '@testing-library/jest-dom/extend-expect'

/**
 * Create a mock fetch response per endpoint.
 * @param {URL | string} url the fetch request url
 * @param {Object} config the fetch request configuration
 * @returns  {Promise<Object>} the mocked fetch response per endpoint
 */
async function mockFetch(url, config) {
  // sbom upload endpoint
  if (url.includes('/sbom')) {
    return {
      json: async () => ({}),
      ok: true,
      status: 200,
      statusText: 'OK',
    }
  }
}

beforeAll(() => {
  /**
   * Mock `window.fetch` for tests
   * @see {@link https://jestjs.io/docs/en/manual-mocks}
   */
  // assuming jest's resetMocks is configured to "true"
  // so we don't need to worry about cleanup. also assumes
  // that a fetch polyfill like `whatwg-fetch` is loaded.
  jest.spyOn(global, 'fetch')
})

beforeEach(() => {
  fetch.mockImplementation(mockFetch)
})
