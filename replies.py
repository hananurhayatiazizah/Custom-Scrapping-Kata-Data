
import os
import requests
import pandas as pd

URL_POSTINGAN = (
    "https://x.com/detikcom/status/1944759450113659310"
)

API_URL = "https://api.twitterapis.com/twitter/tweet/replies"


def main():
    api_key = os.getenv("TWITTERAPIS_KEY")

    if not api_key:
        print("API key belum disiapkan.")
        print("Atur TWITTERAPIS_KEY di terminal VS Code.")
        return

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    params = {
        "url": URL_POSTINGAN,
        "compact": "1"
    }

    print("Mengirim satu permintaan untuk mengambil replies...")

    try:
        response = requests.get(
            API_URL,
            headers=headers,
            params=params,
            timeout=30
        )

        print("Status HTTP:", response.status_code)

        if response.status_code != 200:
            print("Permintaan gagal.")
            print("Detail:", response.text[:500])
            return

        
        semua_replies = []
        cursor = None
        batas_halaman = 3

        for halaman in range(batas_halaman):
            params = {
                "url": URL_POSTINGAN,
                "compact": "1"
            }

            if cursor:
                params["cursor"] = cursor

            print(f"Mengambil halaman {halaman + 1}...")

            response = requests.get(
                API_URL,
                headers=headers,
                params=params,
                timeout=30
            )

            print("Status HTTP:", response.status_code)

            if response.status_code != 200:
                print("Permintaan gagal:", response.text[:500])
                break

            hasil = response.json()
            replies = hasil.get("tweets", [])

            if not replies:
                print("Tidak ada replies pada halaman ini.")
                break

            semua_replies.extend(replies)
            cursor = hasil.get("next_cursor")

            if not cursor:
                print("Tidak ada halaman berikutnya.")
                break

        if not semua_replies:
            print("Tidak ada komentar yang berhasil diambil.")
            return

        data = []

        for reply in semua_replies:
            author = reply.get("author") or {}

            data.append({
                "id_komentar": reply.get("id", ""),
                "komentar": reply.get("text", ""),
                "tanggal": reply.get("created_at", ""),
                "username": author.get("username", ""),
                "likes": reply.get("favorite_count", 0),
                "url": reply.get("url", ""),
                "id_postingan_induk": (
                    reply.get("in_reply_to_status_id", "")
                )
            })

        df = pd.DataFrame(data)
        df = df.drop_duplicates(subset=["id_komentar"])

        df.to_csv(
            "komentar_x.csv",
            index=False,
            encoding="utf-8-sig"
        )

        print("Jumlah replies unik:", len(df))
        print("File berhasil dibuat: komentar_x.csv")
        print(df[["komentar", "tanggal"]].head())


    except requests.RequestException as error:
        print("Kesalahan koneksi:", error)
    except ValueError:
        print("Respons API bukan JSON yang valid.")


if __name__ == "__main__":
    main()
